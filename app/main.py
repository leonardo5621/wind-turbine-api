from fastapi import FastAPI
from routers import health, assets, measurements

app = FastAPI()

app.include_router(health.router)
app.include_router(assets.router)
app.include_router(measurements.router)