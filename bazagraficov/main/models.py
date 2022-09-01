from django.db import models



class admingrafic(models.Model):
    text = models.CharField(max_length=200,verbose_name='График')
    decimalx=models.CharField(max_length=200,verbose_name='ось x')
    decimaly = models.CharField(max_length=200,verbose_name='ось y')


    def __str__(self):
        return f'{self.text[:20]}'

