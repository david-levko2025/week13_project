from fastapi import APIRouter, FastAPI
import uvicorn
import routes



app = FastAPI()

app.include_router(routes.router,prefix="/ip",tags=["IP"])


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)