from django.contrib import admin
from .models import Blog, BlogComment, Contact, Blog_category

# Register your models here.

class Blogs(admin.ModelAdmin):
    list_display=("id","name","Blog_category",'is_verified','is_popular','read')
admin.site.register(Blog,Blogs),

class blogscomments(admin.ModelAdmin):
    list_display=('id','author','blog','comment_date','description')
admin.site.register(BlogComment,blogscomments)

admin.site.register(Contact)
admin.site.register(Blog_category)