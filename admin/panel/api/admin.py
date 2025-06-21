from django.contrib import admin
from .models import Tag, TelegramUser, Task


class TagInline(admin.TabularInline):
    model = Task.tags.through
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    display_fields = ["name", "user"]
    search_fields = ["name"]
    list_filter = ["user"]
    

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    display_fields = ["user_id", "username"]
    search_fields = ["user_id", "username"]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [
        TagInline
    ]
    fields = [
        "name",
        "user",
        "compleated_by_user",
        "is_important",
        "notificate",
    ]
    display_fields = [
        "name",
        "user",
        "is_important",
        "notificate"
    ]
    list_filter = ["project"]
    search_fields = ["name"]
