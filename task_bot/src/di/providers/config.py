from dishka import Provider, Scope, provide
from src.core.config import Config

class ConfigProvider(Provider):
    scope = Scope.APP
    
    @provide
    async def get_config() -> Config:
        return Config()