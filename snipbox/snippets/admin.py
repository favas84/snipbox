from django.contrib import admin

from snippets.models import Tag, Snippet


class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on", "modified_on",
                    "created_by"]
    exclude = ('created_by', 'modified_by')
    search_fields = ("title", )
    ordering = ("title",)

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
            obj.modified_by = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)

class SnippetAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_on", "modified_on")
    exclude = ('created_by', 'modified_by')
    search_fields = ("title", "note")
    list_filter = ("created_on", "tags")
    ordering = ("-created_on",)

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
            obj.modified_by = request.user
        super(SnippetAdmin, self).save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)
admin.site.register(Snippet, SnippetAdmin)
