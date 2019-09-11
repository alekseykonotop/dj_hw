from django.contrib import admin
from .models import Table, FilePath

# Register your models here.


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'serial_number', )


admin.site.register(Table, TableAdmin)


class FilePathAdmin(admin.ModelAdmin):
    list_display = ('file_name', )


admin.site.register(FilePath, FilePathAdmin)

