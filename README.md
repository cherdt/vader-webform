VADER web
=========
[![Build Status](https://travis-ci.org/cherdt/vader-webform.svg?branch=master)](https://travis-ci.org/cherdt/vader-webform)

A web form that analyzes text and provides VADER sentiment analysis scores as you type.

An example is available at https://osric.com/chris/sentiment-analysis/


How to use
----------

You can run this locally using the prebuilt Docker image:

    sudo docker run -p 9600:9600 cherdt/vader-form:latest

Then visit http://localhost:9600


Modifying the code
------------------

If you'd like to make modifications, you'll likely want to run the code
via the Flask development server for testing.

Steps on how to set up a Python virtual environment and run Flask:

    git clone https://github.com/cherdt/vader-webform.git 
    cd vader-webform
    python3 -m venv venv
    source venv/bin/activate
    cd vader
    pip install -r requirements.txt
    python installation.py
    export FLASK_APP=vader-web.py
    flask run


Build the Docker image
----------------------

From the same directory as the `README.md` file:

    sudo docker build --tag <username>/vader-form:latest -f ./docker/Dockerfile .


More information
----------------

* [NLTK](https://www.nltk.org/)
* [VADER](https://www.nltk.org/_modules/nltk/sentiment/vader.html)

