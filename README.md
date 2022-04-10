
# Introduction
This repository contains the code examples with adaptions of the book "Architecture Patterns with Python".
The link of the book is [here](https://www.cosmicpython.com/)

## Requirements
- Python 3.8+
- Pytest
- PostgreSQL
- SQLAlchemy

## Instructions to run the project
1. Clone the project to your local machine
2. Go to the directory you want and create a virtualenv with the command `python -m venv <your_virtualenv>`
3. Active your virtualenv with the command `source <your_virtualenv>/bin/activate`
4. Go to the project root and install project dependencies with the command `pip install -r requirements.txt`
5. Create a `.env` file at the root of the project (See the file `.env_example` in this repository)

Done!! Now you need to run a docker container with Postgres

## Configuring a container of Postgres
1. Firstly, install Docker. If you already have it installed, skip this step. Otherwise, check the official documentation to install

[Docker Documentation](https://docs.docker.com/get-docker/)

2. Create a PostgreSQL container with the command
`docker container run -d -p <host_port>:5432 --name <name_of_container> -e POSTGRES_USER=<your_user> -e POSTGRES_PASSWORD=<your_password> -e POSTGRES_DB=<your_db> postgres:latest`

    2.1. Example:
        To run a container named `mypostgres` on the port `5433` with the database name `mydb`, the username `admin` and the password `root`the command is:
      
        docker container run -d -p 5433:5432 --name mypostgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=root -e POSTGRES_DB=mydb postgres:latest
      
3. After that, add the environment variable `POSTGRES_URL="postgresql+psycopg2://user:password@host:port/dbname"` into your `.env` file
4. Add the other environment variable `API_URL="http://localhost:4200"` (or another port different of `4200`) to run the API

That's it. :)
