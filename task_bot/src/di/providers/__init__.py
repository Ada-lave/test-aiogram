from .config import ConfigProvider
from .service import ServiceProvider
from .api_client import ApiClientProvider
from dishka import Provider

def get_providers() -> list[Provider]:
    return [
        ConfigProvider,
        ApiClientProvider,
        ServiceProvider,
    ]