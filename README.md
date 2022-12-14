# Favourite Music Full Stack Web App

## Features:

- Home Page
- Page for showing a list of all the favourite music
- Page for showing a list of all the opinions
- Page for showing both the favourite music and the opinions
- Page for creating Favorite Music
- Page for creating opinions about the favourite music
- Abaility to update and delete favourite music and opinions

## Fullfiled Requirements:

- Python, django for the backend and Template langauge for the frontend
- Docker for containerization 
- PostgreSQL database

## Running the Project:

```
$ git clone the_url_to_this_repo
$ cd inside "batool-django" poetry project
$ run >> poetry install
$ activiate the powershell by running >> poetry shell
$ make sure you have Docker installed on your machine, and open it
$ run >> docker-compose build
$ run >> docker-compose up
$ run >>> docker-compose up -d, as to not keep interuppting the server and shutting it down constantly
$ instead of shutting down the server and losing the data, with >> $ docker-compose down
	instead run >>> docker-compose stop
		        >>> docker-compose start
```