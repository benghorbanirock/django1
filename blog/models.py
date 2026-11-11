from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title=models.CharField(_('MENU'),max_length=50)
    content=RichTextField(config_name='default')
    created_at=models.DateTimeField(_('Time:'),default=timezone.now)
    author=models.ForeignKey(User,verbose_name=_('writter:'),on_delete=models.CASCADE)
    image=models.ImageField(_('photo:'),upload_to='blogs/',blank=True,null=True)
    category=models.ForeignKey('Category',verbose_name=_("دسته بندی:"),on_delete=models.CASCADE,blank=True,null=True)
    tags=models.ManyToManyField('Tag',verbose_name=_('tags:'),related_name='blogs',blank=True,null=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    title=models.CharField(_("MENU"),max_length=50)
    slug=models.SlugField(_("lutin name:"))
    published_to=models.DateTimeField(_('Time:'),auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.title


class Tag(models.Model):
    title=models.CharField(_('menu'),max_length=50)
    slug=models.SlugField(_('latin menu:'))
    published_at=models.DateTimeField(_('time:'),auto_now=False,auto_now_add=True)
    uplode_to=models.DateTimeField(_('upgrate date:'),auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    blog=models.ForeignKey('Blog',verbose_name=_('maghalrh:'),related_name='command',on_delete=models.CASCADE)
    name=models.CharField(_('name:'),max_length=100)
    email=models.EmailField(_('email:'),max_length=254)
    message=models.TextField(_('message:'))
    date=models.DateField(_('date:'),auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='comment'
        verbose_name_plural='comments'

    def __str__(self):
        return self.email
