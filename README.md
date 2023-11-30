# Wind Turbines API

Project of a Wind Turbine Data API. It has been written in Python using FastAPI and SQLAlchemy as the ORM to interact with a Postgres database.

The application data is provided from a set of CSV files that can be loaded into the postgres database to interact with it.

## Project Structure

This project is divided as follows:

- `app`: Place where the entire API application source code is located.
- `data_sources`: CSV files containing the wind turbines data.
- `jobs`: Module containing jobs that can be launched to perform specific tasks. Most notably, loading the CSV files data into postgres.

## Running the Server

To run the API server locally, there are two main options:

- Running locally with the uvicorn command, **make sure you are placed inside the `app` folder to run this command**:
```
   uvicorn main.app
```

- Running with the provided `docker-compose.yaml` file:
  The `docker-compose` file will take care of setting up the postgres database and the API server. The backend will run using a pre-built image available in this [Docker Hub Repository](https://hub.docker.com/repository/docker/leo5621/wind-turbine-api/general)
```
   docker compose up -d
```

*Some of the routes will include a trailing slash `/` at the end. Make sure to check the `/docs` to see which are the correct ones.*

![Screenshot from 2023-11-30 11-12-39](https://github.com/leonardo5621/wind-turbine-api/assets/30439454/a53297eb-0624-4626-80e3-e509322d267e)

## Mean Calculation Route Example

Example of a call for the mean calculation route, supposing the server is running locally:

Endpoint: `http://127.0.0.1:8000/measurements/mean`

Method: POST

Body:
```
{
	"asset_ids": [101, 102, 103],
	"startTime": 2069586102, // Wednesday, August 1, 2035 13:01:42 (UTC)
	"endTime": 2069672502, // Thursday, August 2, 2035 13:01:42 (UTC)
	"metric": "power"
}
```

**Response**:

```
[
	{
		"asset_name": "WTG 01",
		"mean": 1809.7589554166661
	},
	{
		"asset_name": "WTG 02",
		"mean": 1757.6594918750004
	},
	{
		"asset_name": "WTG 03",
		"mean": 1780.109238541667
	}
]
```
## Loading data into the database

You can run the `init_db_script.py` to have the CSV files data loaded into the postgres database. The data will be loaded into the database only if the script succeeds, otherwise the entire transaction will rolled back.

```
   python init_db_script.py
```
## Environment Variables
Both for running the server and the data loading job, make sure to have the following variables populated into your environment:
```
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=turbines
```

## Possible improvements

There are also improvements that can be brought to this project, here are some of them:

- Include other metric calculation routes into the API.
- Include tracing and metrics intrumentation for server monitoring.
- Create a CI pipeline to check code quality for new pull-requests.
- Creation of custom error handling middlewares to provided more detail why an API call has failed.

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/reference/): Official FastAPI reference and tutorials.
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/): Official Documentation for SQLAlchemy usage.
- [Pydantic API Documentation](https://docs.pydantic.dev/latest/api/base_model/): Official Pydantic Documentation 


 


