from fastapi import APIRouter 

router = APIRouter(prefix='/ip')

@router.post("/")
def send_ip(ip_and_landmarks: dict) -> bool:
    pass 
  #     return bool