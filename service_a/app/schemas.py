from pydantic import BaseModel, IPvAnyAddress


class IPAddress(BaseModel):
    ip : IPvAnyAddress


class CleanData(BaseModel):
    ip: str
    lat: float
    lon: float