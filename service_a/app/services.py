import requests
from schemas import CleanData
from core.config import setting


class GeoIPService:
    GEO_API_URL = setting.GEO_API_URL

    def lookup(self, ip: str) -> CleanData:
        response = requests.get(f"{self.GEO_API_URL}{ip}")
        response.raise_for_status()
        data = response.json()

        return CleanData(
            ip=data.get("query"),
            lat=data.get("lat"),
            lon=data.get("lon")
        )