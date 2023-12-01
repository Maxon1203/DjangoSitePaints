

# Create your models here.
from django.db import models

class Painting(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    size = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)  # например, масляная краска, акварель и т.д.
    image = models.ImageField(upload_to='resources/')

    def __str__(self):
        return self.title


class Review(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()  # оценка от 1 до 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} on {self.painting.title}"
