"""FHIR VALUESETS SERVER.

An implementation of fhir valuesets
"""
import os
import re
import ast
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('fhir_valuesets/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='sil-valuesets-server',
    version=version,
    license='SIL',
    url='https://github.com/savannahinformatics/slade360-valuesets-server',
    author='Brian Ogollah',
    author_email='brian.ogollah@savannahinformatics.com',
    description='A basic server for FHIR Valuesets.',
    long_description=README,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'dj-database-url==0.4.0',
        'ipython==4.2.0',
        'Django~=1.10a1',
        'django-filter==0.13.0',
        'djangorestframework~=3.3.3',
        'psycopg2==2.6.1',
        'gunicorn==19.4.5',
        'Markdown==2.6.5',
        'whitenoise==2.0.6',
        'ujson==1.34',
        'Fabric3',
        'Click==6.2',
        'sil_data_fixtures==1.0.0',
    ],
    keywords='FHIR Profiling Slicing',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: SIL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Clinical Informatics :: Interoperability',
    ],
    scripts=[
        'bin/valuesets_manage',
    ]
)
