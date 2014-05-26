#!/usr/bin/env python
import os
import sys
import logging
import subprocess

from lib.environ import setup_environ
setup_environ()

# Don't allow `runserver` or `shell`

if 'runserver' in sys.argv:
    logging.warn('You should serve your local instance with dev_appserver. See `serve.sh`')
    subprocess.call('./serve.sh')


if 'shell' in sys.argv:
    logging.warn('You should run the shell with ./shell.py, see for more info.')
    subprocess.call('./shell.py')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
