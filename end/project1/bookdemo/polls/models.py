from django.db import models

# Create your models here.


class Title(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Alter(models.Model):
    choice = models.CharField(max_length=10)
    num = models.FloatField(max_length=10, default=10)
    title = models.ForeignKey(Title,on_delete=models.CASCADE,related_name="alters")

    def __str__(self):
        return self.choice



