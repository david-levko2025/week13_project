from fastapi import APIRouter, HTTPException
from schemas import CleanGeoData, IPAddress
from services import GeoIPService
import json


router = APIRouter()
geo_service = GeoIPService()


@router.post("/lookup", response_model=CleanGeoData)
def lookup_ip(data: json):
    try:
        return geo_service.lookup(str(data.ip))
    except Exception:
        raise HTTPException(status_code=500, detail="ip look failed")
    

# @router.get("/")
