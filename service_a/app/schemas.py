from pydantic import BaseModel, IPvAnyAddress


class IPAddress(BaseModel):
    ip : IPvAnyAddress


class CleanData(IPAddress):
    lat: float
    lon: float