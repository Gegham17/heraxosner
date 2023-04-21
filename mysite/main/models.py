from django.db import models

# Create your models here.
class Heraxos(models.Model):
    
    name = models.CharField('Heraxos name', max_length=50)
    price = models.PositiveIntegerField('Heraxos price')
    img = models.ImageField('Heraxos image', upload_to='Heraxos image')

    def __str__(self):
        return self.name
