from django.contrib import admin

from snippets.models import Tag, Snippet


class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on", "modified_on",
                    "created_by"]
    search_fields = ("title", )
    ordering = ("title",)

class SnippetAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_on", "modified_on")
    search_fields = ("title", "note")
    list_filter = ("created_on", "tags")
    ordering = ("-created_on",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Snippet, SnippetAdmin)
