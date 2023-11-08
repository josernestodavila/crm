from django.contrib import admin

from .models import Contact, Provider, ProviderOrganization


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone_number",
    )
    search_fields = (
        "name",
        "email",
    )


class ProviderInline(admin.TabularInline):
    model = Provider


@admin.register(ProviderOrganization)
class ProviderOrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "url",
    )
    search_fields = ("name",)

    inlines = [ProviderInline]
