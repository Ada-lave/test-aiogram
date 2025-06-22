from dishka import make_async_container
from .providers import get_providers

def get_container():
    return make_async_container(*get_providers())