from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BibleStudy, Scripture, Note
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(BibleStudy)
class BibleStudyAdmin(ImportExportModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "user__username")


@admin.register(Scripture)
class ScriptureAdmin(ImportExportModelAdmin):
    list_display = ("verse", "study", "order")
    list_filter = ("study",)
    search_fields = ("verse", "study__title")


@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin):
    list_display = ("content_preview", "study", "scripture", "created_at")
    list_filter = ("study", "scripture")
    search_fields = ("content", "study__title", "scripture__verse")

    def content_preview(self, obj):
        return obj.content[
            :50
        ]  # Shows the first 50 characters of the note for a preview
