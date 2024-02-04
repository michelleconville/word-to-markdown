from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "markdown_content",
    )
    list_filter = ("file",)
