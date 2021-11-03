from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products')


class Review(models.Model):
    text = models.TextField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    def __str__(self):
        return self.product.title



