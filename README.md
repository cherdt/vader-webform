VADER web
=========

A web form that analyzes text and provides VADER sentiment analysis scores as you type.

How to use
----------

You can run this locally using the prebuilt Docker image:

    sudo docker run -p 9600:9600 cherdt/vader-form:latest

Then visit http://localhost:9600

Modifying the code
------------------

Some steps on how to set up a Python virtual environment and modify the code:

* git clone https://github.com/cherdt/vader-webform.git 
* cd vader-webform
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* export FLASK_APP=vader-web.py
* cd vader
* flask run

Build the Docker image
----------------------

From the same directory as the `README.md` file:

    sudo docker build -f ./docker/Dockerfile . --tag <username>/vader-form:latest

More information
----------------

* [NLTK](https://www.nltk.org/)
* [VADER](https://www.nltk.org/_modules/nltk/sentiment/vader.html)

