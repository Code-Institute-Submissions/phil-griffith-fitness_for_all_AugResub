from django.contrib import admin
from .models import MemberBlog

# Register your models here.


class MemberBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('user','date',)
    list_display = (
        'title',
        'user',        
    )


admin.site.register(MemberBlog, MemberBlogAdmin)
