import requests
from schemas import CleanGeoData


class GeoIPService:
    GEO_API_URL = "http://ip-api.com/json/"

    def lookup(self, ip: str) -> CleanGeoData:
        response = requests.get(f"{self.GEO_API_URL}{ip}", timeout=5)
        response.raise_for_status()
        data = response.json()

        return CleanGeoData(
            ip=data.get("query"),
            lat=data.get("lat"),
            lon=data.get("lon"),
            country=data.get("country"),
            city=data.get("city"),
        )

