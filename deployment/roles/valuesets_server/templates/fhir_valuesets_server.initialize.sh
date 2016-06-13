#! /usr/bin/env bash
set -e
source {{valuesets_install_dir}}/valuesets_env.sh &&\
    source {{valuesets_venv_dir}}/bin/activate &&\
    {{django_manage}} migrate
