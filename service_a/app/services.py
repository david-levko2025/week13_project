import requests
from schemas import CleanData


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