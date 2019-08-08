from django.contrib import admin

from api.models import Client, Proposal, Product, Response
from users.models import User


class ClientInline(admin.TabularInline):
    model = Client
    extra = 0


class UserAdmin(admin.ModelAdmin):
   inlines = [ClientInline]


class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0


class ProposalAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Response)
admin.site.register(Proposal, ProposalAdmin)
