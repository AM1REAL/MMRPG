from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Response)
admin.site.register(User)
