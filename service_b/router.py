from fastapi import APIRouter 
from schema import IPData
from storege import DBCrud


router = APIRouter(prefix='/ip')

@router.post("/")
def send_ip(data: IPData) -> bool:
    DBCrud.add_data(data)
    #     return bool