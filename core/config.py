from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    REDIS_USER : str
    REDIS_PORT : int
    REDIS_PASSWORD : str
    REDIS_HOST : str

    GEO_API_URL :str

    model_config = SettingsConfigDict(env_prefix="")

setting = Settings() # type: ignore
