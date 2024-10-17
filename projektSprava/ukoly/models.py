from django.db import models
from django.contrib.auth.models import User

class Ukol(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)
    datum_ukonceni = models.DateTimeField(null=True, blank=True)
    dokoncen = models.BooleanField(default=False)
    vlastnik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazev

