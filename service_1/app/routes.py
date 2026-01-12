from fastapi import APIRouter, HTTPException
from schemas import CleanGeoData, IPAddress
from services import GeoIPService


router = APIRouter()
geo_service = GeoIPService()

@router.post("/lookup", response_model=CleanGeoData)
def lookup_ip(data: IPAddress):
    try:
        return geo_service.lookup(str(data.ip))
    except Exception:
        raise HTTPException(status_code=500, detail="Geo lookup failed")