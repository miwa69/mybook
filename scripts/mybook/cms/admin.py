from django.contrib import admin
from cms.models import Book, Impression


class bookAdmin(admin.ModelAdmin):
  list_display = ('name', 'upper_case_name')

  def upper_case_name(self, obj):
    return ("{0}:{1}円").format(obj.name, obj.publisher)
  upper_case_name.short_description = 'テストフィールドf'


admin.site.register(Book, bookAdmin)
admin.site.register(Impression)
