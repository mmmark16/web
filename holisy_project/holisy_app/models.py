from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователь"""
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    birth_date = models.DateField(null=True, blank=True)
    post = models.CharField(max_length=32, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=12)


class Room(models.Model):
    """Комната"""
    room_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='Название комнаты', default='room')
    beds_number = models.IntegerField(null=True, blank=True, verbose_name='Количество мест')
    day_cost = models.IntegerField(null=True, blank=True, verbose_name='Стоимость за сутки')
    room_class = models.CharField(max_length=32, verbose_name='Класс комнаты')
    photo = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    description = models.TextField(verbose_name='Описание комнаты')


class Service(models.Model):
    """Услуги"""
    service_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')
    cost = models.IntegerField(null=True, blank=True, verbose_name='Стоимость')
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                    related_name='topic_employee_id', verbose_name='Сотрудник')


class Booking(models.Model):
    """Бронирование"""
    status_types = (
        ('p', 'Ожидает оплаты'),
        ('v', 'На подтверждении'),
        ('l', 'В процессе'),
        ('c', 'Завершен')
    )
    booking_id = models.IntegerField(primary_key=True, auto_created=True)
    client_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='topic_client_id',
                                  verbose_name='Гость')
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='topic_room_number',
                                    verbose_name='Номер комнаты')
    arrival_date = models.DateField(null=True, verbose_name='Дата заезда')
    departure_date = models.DateField(null=True, verbose_name='Дата выезда')
    person_count = models.IntegerField(default=1, verbose_name='Количество жильцов')
    result_cost = models.IntegerField(null=True, blank=True, default=0, verbose_name='Счет')
    status = models.CharField(max_length=1, choices=status_types, default='v', verbose_name='Статус')
    services = models.ManyToManyField('Service', related_name='booking_services', verbose_name='Заказанные услуги',
                                      null=True, blank=True)


class Application(models.Model):
    """Заявки"""
    status_types = (
        ('p', 'В ожидании'),
        ('l', 'Выполняется'),
        ('c', 'Выполнен')
    )
    application_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='Название заявки')
    description = models.TextField(verbose_name='Описание заявки')
    status = models.CharField(max_length=1, choices=status_types, verbose_name='Статус')
    employee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                    related_name='topic_manager_id', verbose_name='Сотрудник')
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, related_name='topic_booking_id',
                                   verbose_name='Номер брони')
