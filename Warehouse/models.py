from django.db import models

# Create your models here.

class Mahsulot(models.Model):
    mahsulot_nomi = models.CharField(max_length=255)
    mahsulot_kodi = models.IntegerField()
    
    def __str__(self):
        return self.mahsulot_nomi

class Xomashyo(models.Model):
    xomashyo_nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.xomashyo_nomi

class Mahsulot_Xomashyo(models.Model):
    product_id = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Xomashyo, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f'{self.product_id}'

class Omborxona(models.Model):
    material_id = models.ForeignKey(Xomashyo, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.material_id}'


