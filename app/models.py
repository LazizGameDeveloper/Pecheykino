from django.db import models
from django.db.models.deletion import DO_NOTHING


class Unit(models.Model):
    name = models.CharField("Ед измереения", max_length=20)
    
    class Meta:
        verbose_name = "Ед измерения"
        verbose_name_plural = "Ед измерения"

    def __str__(self) -> str:
        return self.name

class Provider(models.Model):
    name = models.CharField("Поставщик", max_length=150)
    is_active = models.BooleanField("Активность", default=False)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
    
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name = models.CharField("Название продукта", max_length=70)
    key = models.CharField("Ключ продукта", max_length=50)
    provider = models.ForeignKey(Provider, verbose_name="Поставщик", on_delete=DO_NOTHING)
    price = models.PositiveIntegerField("Цена продукта", default=0)
    unit = models.ForeignKey(Unit, verbose_name="Ед измерения", on_delete=DO_NOTHING)
    amount_in_box = models.CharField("Кол-во в коробке", max_length=10, default=1)
    is_active = models.BooleanField("Активность", default=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

        ordering = ["name", "provider"]

    
    def __str__(self) -> str:
        return self.name
