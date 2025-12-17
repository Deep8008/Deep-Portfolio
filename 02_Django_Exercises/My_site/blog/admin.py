from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'status', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    summernote_widget = {
        'jquery_url': '/static/js/vendor/jquery-3.6.0.min.js',
        'css_url': '/static/js/vendor/bootstrap.min.css',
        'summernote_js': ['/static/js/vendor/summernote-bs4.js'],
        'summernote_css': ['/static/js/vendor/summernote-bs4.min.css'],
    }

admin.site.register(Category)   
admin.site.register(Post, PostAdmin)
