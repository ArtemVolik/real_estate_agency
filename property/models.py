from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    """ Квартира. """
    created_at = models.DateTimeField("Когда создано объявление",
                                      default=timezone.now, db_index=True)
    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)

    town = models.CharField("Город, где находится квартира", max_length=50,
                            db_index=True)
    town_district = models.CharField("Район города, где находится квартира",
                                     max_length=50,
                                     blank=True,
                                     help_text='Чертаново Южное')
    address = models.TextField("Адрес квартиры",
                               help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        "Этаж", max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField("Количество комнат в квартире",
                                       db_index=True)
    living_area = models.IntegerField("количество жилых кв.метров",
                                      null=True, blank=True, db_index=True)

    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    construction_year = models.IntegerField(
        "Год постройки здания", null=True, blank=True, db_index=True)
    new_building = models.NullBooleanField(
        'Новостройка', default=None)
    likes = models.ManyToManyField(
        User, related_name='liked_flats', blank=True,
        verbose_name='Кто лайкнул')

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"

    def get_owner_name(self):
        return ','.join([owner.owner
                         for owner in self.flat_owners.all()])

    def get_owner_phonenumber(self):
        return ','.join([owner.owners_phonenumber
                         for owner in self.flat_owners.all()])

    def get_owner_pure_phone(self):
        return ','.join(
            [str(owner.owners_pure_phone)
             for owner in self.flat_owners.all()])

    get_owner_name.short_description = u'Фио владельца'
    get_owner_phonenumber.short_description = u'Номер владельца'
    get_owner_pure_phone.short_description = u'Нормализованый номер владельца'


class Complaint(models.Model):
    """Жалоба на обьявление. """
    complaint_author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, verbose_name="Кто жаловался")
    complaint_flat = models.ForeignKey(
        Flat, on_delete=models.SET_NULL,
        verbose_name='Квартира, на которую жаловались', null=True)
    complaint_text = models.TextField('Текст жалобы', null=True)


class Owner(models.Model):
    """Владелец квартиры. """
    owner = models.CharField(
        "ФИО владельца", max_length=200, db_index=True)
    owners_phonenumber = models.CharField(
        "Номер владельца", max_length=20, db_index=True)
    owners_pure_phone = PhoneNumberField(
        'Нормализованый номер владельца',
        null=True, blank=True, db_index=True)
    flat_in_property = models.ManyToManyField(
        Flat, related_name='flat_owners', db_index=True)

    def __str__(self):
        return f"{self.owner}, {self.owners_pure_phone}"
