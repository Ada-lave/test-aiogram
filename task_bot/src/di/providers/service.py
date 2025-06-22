from dishka import Provider, Scope, provide

class ServiceProvider(Provider):
    scope = Scope.REQUEST
    
    @provide
    async def get_user_service(): ...
    
    @provide
    async def get_task_service(): ...
    
    @provide
    async def get_tag_service(): ...
    
    @provide
    async def get_project_service(): ...