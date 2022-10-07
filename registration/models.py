from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class RegFields(models.Model):
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name='Вы регестрируетесь как')
    email = models.EmailField(max_length=100, verbose_name='Эл. почта')
    name = models.CharField(max_length=100, verbose_name='ИП или Юр. лицо')
    inn = models.CharField(max_length=15, verbose_name='ИНН')
    city = models.CharField(max_length=100, verbose_name='Ваш город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Дом/стр.')
    office = models.CharField(max_length=10, verbose_name='Офис')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    site = models.CharField(max_length=100, verbose_name='Сайт Вашей компании')
    store = models.BooleanField(blank=True, verbose_name='Магазин')
    regional_store = models.BooleanField(blank=True, verbose_name='Региональная сеть магазинов')
    federal_store = models.BooleanField(blank=True, verbose_name='Федеральная сеть магазинов')
    online_store = models.BooleanField(blank=True, verbose_name='Интернет-магазин')
    car_service = models.BooleanField(blank=True, verbose_name='Автосервис')
    other = models.CharField(max_length=100, blank=True, verbose_name='Прочее')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name

