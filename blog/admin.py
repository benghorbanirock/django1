from django.contrib import admin
from .models import Blog,Category,Tag,Comments

# Register your models here.
#admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog,BlogAdmin)