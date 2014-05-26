import logging, unittest

from google.appengine.datastore import datastore_stub_util
from google.appengine.ext import ndb, testbed


logging.basicConfig()
log = logging.getLogger("ndbtestcase")


class AppEngineTestCase(unittest.TestCase):
    """Common test setup required for testing App Engine-related things.

    You can provide your own default and specific keyword arguments for each
    service stub by implementing properties of the names

        `default_{service_name}_stub_kwargs` and
        `{service_name}_stub_kwargs`

    where {service_name} is one of the names defined in google.appengine.ext.testbed
    """
    @property
    def default_datastore_v3_stub_kwargs(self):
        # By default we assume - possibly wrongly - that tests use the high-
        # replication datastore with the scattered ID policy and require indexes
        # so that tests fail if indexes are missing. We also use sqlite by
        # default because it's faster than the file stub

        cp = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=1)

        return {
            "use_sqlite": True,
            "require_indexes": True,
            "consistency_policy": cp,
            "auto_id_policy": datastore_stub_util.SCATTERED,
        }

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        for service_name, stub_method_name in testbed.INIT_STUB_METHOD_NAMES.items():
            default_kwargs_attr_name = "default_{}_stub_kwargs".format(service_name)
            kwargs_attr_name = "{}_stub_kwargs".format(service_name)

            default_kwargs = getattr(self, default_kwargs_attr_name, {})
            kwargs = getattr(self, kwargs_attr_name, {})

            default_kwargs.update(kwargs)

            try:
                getattr(self.testbed, stub_method_name, lambda: None)()
            except testbed.StubNotSupportedError as e:
                log.warning(
                    "Couldn't initialise stub with error {}. Continuing..."
                    .format(str(e))
                )

        self.clear_datastore()

    def tearDown(self):
        self.clear_datastore()
        self.testbed.deactivate()

    def clear_datastore(self):
        datastore_stub = self.testbed.get_stub(testbed.DATASTORE_SERVICE_NAME)
        datastore_stub.Clear()

    def users_login(self, email, user_id=None, is_admin=False):
        self.testbed.setup_env(
            USER_EMAIL=email,
            USER_ID=user_id or '98211821748316341', # Random ID
            USER_IS_ADMIN=str(int(is_admin)),
            AUTH_DOMAIN='testbed',
            overwrite=True,
        )


NdbTestCase = AppEngineTestCase


if __name__ == '__main__':
    unittest.main()
