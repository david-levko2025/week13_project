from fastapi import APIRouter, FastAPI
import uvicorn
import routes
from services import GeoIPService


app = FastAPI()

app.include_router(routes.router)


if __name__ == "__nain__":
    uvicorn.run(app,host="localhost",port=8000)