from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_header = 'Shop Administration'
admin.site.site_title = 'My Courses'
admin.site.index_title = 'Welcome to the shop administration'


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CoursesAdmin)
