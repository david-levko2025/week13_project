from fastapi import APIRouter, HTTPException
from schemas import CleanData, IPAddress
from services import GeoIPService, SendData


router = APIRouter()
geo_service = GeoIPService()
send_data = SendData()

@router.post("/lookup", response_model=CleanData)
def lookup_ip(data: IPAddress):
    try:
        new_data = geo_service.lookup(str(data.ip)) 
        SendData.send_to_service_b(new_data)
        return geo_service.lookup(str(data.ip)) 
    except Exception:

        raise HTTPException(status_code=500, detail="ip look failed")
    

