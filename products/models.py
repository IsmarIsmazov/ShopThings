from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=155)
    descriptions = models.TextField()
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/products/{self.id}'
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'