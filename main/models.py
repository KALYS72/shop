from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=25, choices=[('есть в наличии', 'in stock'),('нет в наличии', 'out of stock'), ('ожидается', 'pending')])
    image = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return f'[{self.category}] -> {self.title}]'

    
    @property
    def average_rating(self):
        ratings = self.ratings.all()
        values = []
        for rating in ratings:
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0
    
    class Meta:
        ordering = ['id']