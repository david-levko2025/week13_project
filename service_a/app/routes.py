from fastapi import APIRouter, HTTPException
from schemas import CleanData, IPAddress
from services import GeoIPService
import json


router = APIRouter()
geo_service = GeoIPService()


@router.post("/lookup", response_model=CleanData)
def lookup_ip(data: IPAddress):
    try:
        data = geo_service.lookup(str(data.ip))
        return "the check work successfuly"
    except Exception:
        raise HTTPException(status_code=500, detail="ip look failed")