from django.db import models


class LeatherSeat(models.Model):
    brand = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Описание', max_length=4000)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='shop_uploads/leather_seat/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Кожаное седло'
        verbose_name_plural = 'Кожаные седла'

    def __str__(self):
        return '{0} - цена {1} грн'.format(
            self.brand,
            self.price
        )


class CustomSeat(models.Model):
    brand = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Описание', max_length=4000)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='shop_uploads/custom_seat/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Стандартное седло'
        verbose_name_plural = 'Стандартные седла'

    def __str__(self):
        return '{0} - цена {1} грн'.format(
            self.brand,
            self.price
        )


class LimitedSeat(models.Model):
    brand = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Описание', max_length=4000)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='shop_uploads/limited_seat/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Эксклюзивное седло'
        verbose_name_plural = 'Эксклюзивные седла'

    def __str__(self):
        return '{0} - цена {1} грн'.format(
            self.brand,
            self.price
        )


class Bag(models.Model):
    brand = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Описание', max_length=4000)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='shop_uploads/bag/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Сумка'
        verbose_name_plural = 'Сумки'

    def __str__(self):
        return '{0} - цена {1} грн'.format(
            self.brand,
            self.price
        )


class Bike(models.Model):
    brand = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Описание', max_length=4000)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='shop_uploads/bike/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

    def __str__(self):
        return '{0} - цена {1} грн'.format(
            self.brand,
            self.price
        )


class Accessories(models.Model):
    brand = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Описание', max_length=4000)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='shop_uploads/accessories/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'

    def __str__(self):
        return '{0} - цена {1} грн'.format(
            self.brand,
            self.price
        )