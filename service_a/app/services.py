import requests
from schemas import CleanData
import os 
from dotenv import load_dotenv 

class GeoIPService:
    GEO_API_URL = "http://ip-api.com/json/"

    def lookup(self, ip: str) -> CleanData:
        response = requests.get(f"{self.GEO_API_URL}{ip}")
        response.raise_for_status()
        data = response.json()

        return CleanData(
            ip=data.get("query"),
            lat=data.get("lat"),
            lon=data.get("lon")
        )

class SendData:
    host = "localhost"

    def send_to_service_b(self):
        try:
            requests.post(SendData.host)
            return True
        except:
            return False