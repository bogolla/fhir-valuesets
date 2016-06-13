#!/usr/bin/env bash

cd {{valuesets_install_dir}}
source {{valuesets_venv_dir}}/bin/activate
source {{valuesets_install_dir}}/valuesets_env.sh
workers=$(expr $(nproc) \* 2 + 1)

exec gunicorn --workers $workers --bind 127.0.0.1:{{valuesets_port}} fhir_valuesets.configs.wsgi  --access-logfile {{log_dir}}/gunicorn.access.log --error-logfile {{log_dir}}/gunicorn.error.log --log-level info
