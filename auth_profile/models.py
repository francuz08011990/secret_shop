from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    MALE_CHOICES = (('male', 'Мужской'), ('female', 'Женский'))
    phone = models.CharField('Телефон', max_length=15, blank=True, null=True)
    country = models.CharField('Страна', max_length=50, blank=True, null=True)
    region = models.CharField('Область', max_length=50, blank=True, null=True)
    city = models.CharField('Город', max_length=50, blank=True, null=True)
    address = models.CharField('Адрес', max_length=128, blank=True, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    male = models.CharField('Пол', choices=MALE_CHOICES, max_length=128, blank=True, null=True)
    biography = models.TextField('Биография', max_length=4000, blank=True, null=True)
    avatar = models.ImageField(
        'Фото',
        upload_to='user_uploads/avatars/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Профайл пользователя'
        verbose_name_plural = 'Профайлы пользователей'

    def __str__(self):
        return '{0} из {1}, телефон: {2}'.format(
            self.user.get_full_name(),
            self.country,
            self.phone
        )

