from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .choices import HTTPStatusChoice



class UserPassedLink(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", verbose_name=_("user")
    )
    link = models.URLField(_("URL link"))
    status = models.PositiveIntegerField(_("status code"), choices=HTTPStatusChoice.choices, null=True, blank=True)
    checked_at = models.DateTimeField(_("last checked time"), auto_now=True)
    created_at = models.DateTimeField(_("created time"), auto_now_add=True)

    class Meta:
        verbose_name = _("user passed link")
        verbose_name_plural = _("user passed links")

    def __str__(self) -> str:
        return self.link
