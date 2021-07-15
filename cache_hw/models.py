from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Author'

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.CharField(max_length=300)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Post'

    def __str__(self):
        return f'Post: {self.id}'


class Quotes(models.Model):
    quotes = models.CharField(max_length=300)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Quotes'

    def __str__(self):
        return f'Quote: {self.id}'