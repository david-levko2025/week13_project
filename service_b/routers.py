from fastapi import APIRouter 
from schema import IPData
from storege import DBCrud


router = APIRouter(prefix='/ip', tags=["ip"])

@router.post("/")
def send_ip(data: IPData) -> bool:
    if DBCrud.add_data(data):
        return True 
    return False

@router.get("/")
def get_all_data():
    return DBCrud.get_data()

