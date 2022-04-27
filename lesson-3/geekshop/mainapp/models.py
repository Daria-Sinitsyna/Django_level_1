from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64,unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )
    short_disc = models.CharField(
        verbose_name='краткое описание товара',
        max_length=60,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='стоимость продукта',
        max_digits=8,
        decimal_places=2,
        default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'