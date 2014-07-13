"""
Common tools for deploy run shell and the like.
"""

import os
from string import Template
from urllib import urlencode

from fabric.api import *
from fabric.colors import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists
import requests

env.use_ssh_config = True


@task
def pep8():
    """Run Pep8"""
    local("pep8 raxui --exclude='*migrations*','*static*'")


@task
def test(skip_js='False'):
    """Run the test suite"""
    local("rm -rf htmlcov")
    local("coverage run --include='raxui*' --omit='*migration*' manage.py test")
    local("coverage html")
    if skip_js == 'False':
        with lcd('assets'):
            local('node_modules/grunt-cli/bin/grunt jasmine')
    pep8()


@task
def install():
    """Install the node_modules dependencies"""
    local('git submodule update --init')

    local('python manage.py migrate')

    with lcd('assets'), settings(warn_only=True):
        out = local('npm install')
        if out.failed:
            print(red("Problem running npm, did you install node?"))


@task
def watch():
    """Grunt watch development files"""
    with lcd('assets'):
        local('node_modules/grunt-cli/bin/grunt concat less:dev watch')


@task
def compile():
    """Compile assets for production."""
    with lcd('assets'):
        local('node_modules/grunt-cli/bin/grunt less:prod uglify')
