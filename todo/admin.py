from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("done",)


admin.site.register(Tag)
