from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Food(models.Model):
    FOOD_TYPE=[
        ('breakefast','breakfast'),
        ('drinks','drink'),
        ('dinner','diner'),
        ('lunch','launch'),
    ]
    name=models.CharField(max_length=100)
    description=models.CharField(_('explians:'),max_length=50)
    rate=models.IntegerField(_('Rate:'),default=0)
    price=models.IntegerField()
    time=models.IntegerField(_('time:'))
    pud_date=models.DateField(_('date:'),auto_now=False,auto_now_add=True)
    photo=models.ImageField(upload_to='foods/')
    type_food=models.CharField(_('types of food'),max_length=10,choices=FOOD_TYPE,default='drinks')


    def __str__(self):
        return self.name