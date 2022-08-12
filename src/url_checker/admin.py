from django.contrib import admin

from .models import UserPassedLink


class UserPassedLinkAdmin(admin.ModelAdmin):
    model = UserPassedLink
    list_display = ["user", "link", "status"]
    readonly_fields = ["checked_at", "created_at"]


admin.site.register(UserPassedLink, UserPassedLinkAdmin)
