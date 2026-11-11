from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Reservetion(models.Model):
    name=models.CharField(_("name&firstname:"),max_length=200)
    E_mail=models.EmailField(_("email:"),max_length=254)
    phone=models.CharField(_("phone:"),max_length=20)
    number=models.IntegerField(_("num:"))
    date=models.DateField(_("date:"),auto_now=False,auto_now_add=False)
    time=models.TimeField(_("time:"),auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.E_mail