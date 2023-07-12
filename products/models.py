from django.db import models

# Create your models here.

RATE =((i, '★' * i) for i in range(1, 6))

class Category(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=100)
    descroptoin = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    rate = models.IntegerField(choices=RATE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title
# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.CharField(max_length=250)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.author.username}, {self.text}'