import os
from os.path import dirname, abspath
from fabric.api import local, lcd


BASE_DIR = dirname(abspath(__file__))
DEPLOY_PATH = BASE_DIR + '/deployment/'


def test():
    local("tox")


def run():
    local('{}/manage.py runserver 8030'.format(BASE_DIR))


def shell():
    local('{}/manage.py shell'.format(BASE_DIR))


def setup(*args, **kwargs):
    sudoer = '' if 'no-sudo' in args else 'sudo -u postgres '
    with lcd(BASE_DIR):
        local('{} psql -c "DROP DATABASE IF EXISTS sil_valuesets"'.format(
            sudoer))
        local('{} psql -c  "CREATE DATABASE sile_valuesets"'.format(sudoer))
        local('python manage.py migrate')


def load():
    with lcd(BASE_DIR):
        data_files = os.path.join(BASE_DIR, 'fhir_server/data/generated/*.json')
        local('{0}/manage.py bootstrap {1}'.format(BASE_DIR, data_files))


def pypi_deploy():
    with lcd(BASE_DIR):
        local('python setup.py sdist upload -r slade')


def gce_deploy():
    with lcd(DEPLOY_PATH):
        local('ansible-playbook fhir_valuesets.yml')
