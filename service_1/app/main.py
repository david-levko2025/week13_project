from fastapi import APIRouter, FastAPI
from routes import router


app = FastAPI()

app.include_router(router,prefix="/ip",tags=["IP"])


if __name__ == "__nain__"():
    pass