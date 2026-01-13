from pydantic import BaseModel, IPvAnyAddress


class IPAddress(BaseModel):
    ip : IPvAnyAddress


class CleanGeoData(BaseModel):
    ip: str
    lat: float
    lon: float