from fastapi import APIRouter 

router = APIRouter(prefix='/ip')

@router.post("/")
