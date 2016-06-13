from fhir_valuesets.configs.settings import *   # NOQA

DEFAULT_TEST_DB = 'postgres://sil:sil@localhost:5432/test_sil_valuesets'
DATABASES['default']['TEST'] = {
    'default': dj_database_url.config(
        env='TEST_DATABASE_URL',
        default=DEFAULT_TEST_DB,
        conn_max_age=500)
}
