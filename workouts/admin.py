from django.contrib import admin
from .models import Workouts, Category

# Register your models here.


class WorkoutsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'video_url',
        'video_image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Workouts, WorkoutsAdmin)
admin.site.register(Category, CategoryAdmin)
