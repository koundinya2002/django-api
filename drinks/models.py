from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=265)
    description = models.CharField(max_length=265)

    def __str__(self):
        return self.name + ' ' + self.description