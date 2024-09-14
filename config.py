from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    api_key: str
    db_key: str
    db_root_key: str
    db_database : str
    db_user : str
    db_port : int
    nginx_port : int
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()