Sheetgo Challenge Backend
===========
[![Build Status](https://travis-ci.com/GustavoDinizMonteiro/sheetgo-challenge-backend.svg?branch=master)](https://travis-ci.com/GustavoDinizMonteiro/sheetgo-challenge-backend)
[![codecov](https://codecov.io/gh/GustavoDinizMonteiro/flask-api/branch/master/graph/badge.svg)](https://codecov.io/gh/GustavoDinizMonteiro/flask-api)

## API Documentation

<a target="_blank" href="https://book-blog-api.herokuapp.com/apidocs">
    Access swagger reference here
</a>

or

<a target="_blank" href="https://documenter.getpostman.com/view/1420305/SzzkccWp?version=latest">
    Postman reference here
</a>

## Building from source

1. Ensure you have 

   ```Python3``` installed - https://pip.pypa.io/en/stable.    
   ```pip3``` installed - https://pip.pypa.io/en/stable.

1. Clone this repository to your local filesystem (default branch is 'master')

1. with pipenv(recommended)
   ```
    pip3 install pipenv
    pipenv --three
    pipenv shell
    pipenv install
   ```

1. To run the application, run the following command on the project root folder

   ```
    flask run
   ```


### Build

For production you need to provide to enviroment variables:

* `DB_URI`: Url for ProstgreSQL Database

With this you need just run the following commands:

* `pipenv deploy`

and the aplication will start in port 5000. Opitionaly you can use a specific port:

* `gunicorn --bind 0.0.0.0:$PORT app:app`

### Other alternative ways to generate a build.

not yet


## Running the tests

You just need to run the following command:

`pipenv test`


## Contribution guidelines

Not yet