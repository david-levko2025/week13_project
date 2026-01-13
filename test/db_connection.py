from pydantic import BaseModel 

class IPData(BaseModel):
    ip: str 
    lat: str 
    lon: str 

id = IPData(ip="13.34.54.45", lat="jkl", lon="jlkj")


print(id.model_dump_json())