from pydantic import BaseModel, IPvAnyAddress


class IPAddress(BaseModel):
    ip : IPvAnyAddress


class CleanGeoData(BaseModel):
    ip: str
    lat: float | None = None
    lon: float | None = None
    country: str | None = None
    city: str | None = None