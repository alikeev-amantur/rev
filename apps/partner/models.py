from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Establishment(models.Model):
    """
    Represents an establishment model
    """

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to="establishment_logos/",
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    happyhours_start = models.TimeField(null=True, blank=True)
    happyhours_end = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "Establishment: " + self.name


# class QRCode(models.Model):
#     establishment = models.OneToOneField(
#         Establishment, on_delete=models.CASCADE, related_name="qr_code"
#     )
#     qr_code_image = models.ImageField(upload_to="qr_codes/")
#
#     def __str__(self):
#         return f"QR Code for {self.establishment.name}"
