from fastapi import FastAPI
from dotenv import load_dotenv
from routers import health, assets, measurements
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

tags_metadata = [
    {
        "name": "health",
        "description": "Health Check Routes",
    },
    {
        "name": "assets",
        "description": "Operations on the Wind Turbine Assets.",
    },
        {
        "name": "measurements",
        "description": "Operations on the Wind Turbine Measurements.",
    },
]

app = FastAPI(
    title="Wind Turbines API",
    description="API for querying Wind Turbine Assets metrics",
    version="v1.0.0",
    openapi_tags=tags_metadata
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(assets.router)
app.include_router(measurements.router)