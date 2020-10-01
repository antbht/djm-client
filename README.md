# Dejamobile Take Home - Client

A client to managed digitalized card. This is based on project djm_sdk which embeds all the stuff to request the backend API (djm_back).


## How to use ?

### Prerequisite 

- Have python 3.8 installed
- Have `virtualenv` python package installed
- Clone this project into your workspace

### Initialize the project

This is a Python project. For good practices and environments isolation purpose, we advise to run it into a virtual envrionment.

```lang=bash
cd /path/to/djm_client
virtualenv .
source bin/activate
pip install -r requirements.txt
```

### Run the unit tests

Functions of this project are covered by unit tests. To execute them, please run this script

```lang=bash
cd /path/to/djm_client
source bin/activate
python -m unittest unit_tests/*.py
```

### Run the app

To run the APP, you have to install it into its own environment. It creates an executable which starts the client CLI.

```lang=bash
cd /path/to/djm_client
source bin/activate
pip install -e .
djm-client --host 127.0.0.1 --ip 8000
```

This start a CLI which can be use to manage your digitalized cards.



### Use the sample of ci script

This script simulates a CI script which could be implements for GitlabCI, jenkins, ... CI/CD platforms. It :
- Initialize the virtualenv
- Run unit tests
- Build the wheel

```lang=bash
cd /path/to/djm_client
bash ci_script.sh
```
