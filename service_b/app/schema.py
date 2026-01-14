from pydantic import BaseModel 

class IPData(BaseModel):
    ip: str 
    lat: str 
    lon: str 

