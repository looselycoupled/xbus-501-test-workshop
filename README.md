Overview
--------

This repository contains the automated testing workshop for the Georgetown University, Data Science Certificate Program, XBUS-501 Software Engineering for Data class.

In order to complete the workshop, clone this repository and then fill in the missing tests.  If time allows feel free to continue adding tests or add more functionality to the buildings or vehicles modules for testing.

Setup
-----

To download the repository, run `git clone` from the command line as follows:

    git clone git@github.com:looselycoupled/xbus-501-test-workshop.git

Next, install the project dependencies using `pip` and the supplied `requirements.txt` file.

    pip install -r requirements.txt

Tests
-----

To execute the tests, use the following command:

    nosetests -v --with-coverage --cover-package=motorsports --cover-inclusive --cover-erase tests
