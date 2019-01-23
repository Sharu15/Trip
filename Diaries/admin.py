from django.contrib import admin
from Diaries.models import Post,Plan,Comment,Profile
# Register your models here.
admin.site.register(Post)
admin.site.register(Plan)
admin.site.register(Comment)
admin.site.register(Profile)