Slade360-Valueset-Server
========================

This is an API server that defines a set of codes from [FHIR valuesets](https://www.hl7.org/fhir/terminologies-valuesets.html) 

Getting Started
===============

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisities
--------------

You will need the following installed before you can run the server::

    Python3.5.1
    Python3.5.1-dev


Setting up project environment
------------------------------

Clone and go to the project directory::

    $ git clone git@github.com:savannahinformatics/slade360-valuesets-server.git
    $ cd path/to/project/directory/slade360-valuesets-server
    

Create a py3.5.1 virtual environment::

    $ mkvirtualenv --python=/usr/bin/python3.5.1 env_name # env_name is the name of your virtual environment


Configure environment variables to use whenever the virtual environment is activated.
The SECRETE_KEY provided in settings is a default that should be overridden by the one you are required to provide here::

    $ vim ~/{virtualenv_folder_path}/{env_name}/bin/postactivate
    # Add the following lines to the open file and then save.
    #
    # cd ~/SIL/fhir-valuesets/
    # export DATABASE_URL="postgresql://localhost/sil_valuesets"
    # export TEST_DATABASE_URL="postgresql://localhost/test_sil_valuesets"
    # export SECRET_KEY="please-change-this"


Install the requirements::

    $ pip install -r requirements.txt 

Run the following commands from the project base directory to setup the project database::

    $ fab setup  #  creates the databbase and runs migrations
    $ fab load  #  loads default data to your database
    $ fab run  #  runs the server at http://localhost:8030/

You can browse the API at http://localhost:8030/

## Running the tests

Install the test requirements and run test command::

$ pip install -r requirements-test.txt 
$ fab test

Deployment
----------

To deploy this project create a python2 virtual environment::

    $ mkvirtualenv --python=/usr/bin/python2.7 env_name # env_name is the name of your virtual environment

Install the deployment dependencies to your virtual environment::

    $ pip install -r requirements-deploy.txt


Run the deployment command to deploy the project to gce::

    $ fab gce_deploy


Authors
-------

* [Brian Ogollah](https://github.com/bogolla)
