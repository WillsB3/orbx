import unittest

from google.appengine.ext import ndb

from ndbtestcase import AppEngineTestCase


class Thing(ndb.Model):
    stuff = ndb.StringProperty()


class ATestCase(AppEngineTestCase):
    """Example App Engine testcase"""

    def test_thing_exists(self):
        self.thing = Thing(stuff="Hi")
        self.thing.put()
        self.assertEquals(Thing.query().count(), 1)


if __name__ == '__main__':
    unittest.main()
