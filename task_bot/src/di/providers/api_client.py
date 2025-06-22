from dishka import Provider, Scope, provide
from src.core.config import Config
from src.infra.api_client import ApiClient

class ApiClientProvider(Provider):
    scope = Scope.REQUEST
    
    @provide
    async def get_api_client(self, config: Config) -> ApiClient:
        return ApiClient(base_url=config.api_config.url)