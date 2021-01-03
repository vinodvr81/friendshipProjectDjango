from django.db import models

# Create your models here.


# Create your models here.
class Note(models.Model):
    Title = models.CharField('name', max_length=200)
    Text = models.TextField('Desc', max_length=500, blank=True)

    def __str__(self):
        return '%s' % (self.name)
