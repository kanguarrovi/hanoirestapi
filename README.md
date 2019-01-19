# hanoi-rest-api

A simple Python3 Flask REST API which solves the towers of Hanoi game in the minor quantity of steps possible.

Reference: https://www.mathsisfun.com/games/towerofhanoi.html

## Installation

Clone this repository

	$ git clone https://github.com/kanguarrovi/hanoirestapi.git

Create a virtualenv (on Debian-based Linux)

    $ cd hanoirestapi
	$ python3 -m venv venv
	$ source venv/bin/activate

Upgrade pip if it is required 

	$ pip install --upgrade pip

Install requirements 

	$ pip install -r requirements.txt
	

## Run in development

	$ python hanoi_rest_api.py

	
## Test with curl (in another terminal)

This example will show the optimal solution of the towers of Hanoi if it had 4 disks:

    $ curl http://127.0.0.1:5000/hanoirestapi -d "disks=4"





