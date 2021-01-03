from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('name', max_length=200)
    email = models.EmailField('Email', blank=True)
    headshot = models.ImageField(upload_to='img', blank=True)
    text = models.TextField('Desc', max_length=500, blank=True)

    def __str__(self):
        return '%s' % (self.name)
