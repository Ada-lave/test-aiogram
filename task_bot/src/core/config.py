from pydantic_settings import BaseSettings, SettingsConfigDict

class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="API_")
    url: str

class RedisConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_")
    url: str
    
class Config:
    api_config: ApiConfig = ApiConfig()
    redis_config: RedisConfig = RedisConfig()