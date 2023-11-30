# Wind Turbines API

Project of wind turbine data API. It has been written in Python using FastAPI and SQLAlchemy as the ORM to interact with a postgres database.

The application data is provided from a set of CSV files that can be loaded into the postgres databas to interact with it.

## Project Structure

This project is divided as follows:

- app folder: Place where the entire API application source code is located
- data_sources: CSV files containing the wind turbines data
- job: Module containing jos that can be launched to perform specific tasks. Most notably, loading the CSV files data into the postgres database.

## Running the Server

To run the API server locally, there are two main options:


