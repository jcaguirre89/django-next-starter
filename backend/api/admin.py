from django.contrib import admin

from api.models import MyModel
from users.models import User

# Register your models here.
class MyModelInline(admin.TabularInline):
    model = MyModel
    extra = 0


class UserAdmin(admin.ModelAdmin):
   inlines = [MyModelInline]


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
