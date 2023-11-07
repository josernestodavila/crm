from django.db import models

from .contacts import Contact
from .mixins import TimeStampedMixin


class ProviderOrganization(TimeStampedMixin, models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField()
    contacts = models.ManyToManyField(to=Contact, through="Provider")

    class Meta:
        verbose_name = "Provider Organization"
        verbose_name_plural = "Provider Organizations"

    def __str__(self) -> str:
        return self.name


class Provider(TimeStampedMixin, models.Model):
    provider_organization = models.ForeignKey(to="ProviderOrganization", on_delete=models.CASCADE)
    contact_information = models.ForeignKey(to=Contact, related_name="providers", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self) -> str:
        return self.contact_information.name
