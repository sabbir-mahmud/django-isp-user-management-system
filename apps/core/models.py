# imports
from django.db import models

# information Model


class Isp_info(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


# pop model
class Pop(models.Model):
    pop_name = models.CharField(max_length=200)
    users = models.IntegerField(default=0)
    main_pop_name = models.ForeignKey('self',
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pop_name


# Internet package Model
class Package(models.Model):
    choice_status = (('Active', 'Active'), ('Inactive', 'Inactive'))
    name = models.CharField(max_length=200)
    speed = models.IntegerField()
    ggc = models.IntegerField(default=10, verbose_name='GGC')
    fna = models.IntegerField(default=10, verbose_name='FNA')
    public_ip = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=choice_status)
    price = models.IntegerField()

    def __str__(self):
        return self.name


# Fiber Model
class Fiber(models.Model):
    choice_status = (('Active', 'Active'), ('Stored', 'Stored'), ('Damaged',
                                                                  'Damaged'))
    brand = models.CharField(max_length=200)
    code = models.IntegerField(unique=True)
    metre = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=choice_status)

    def __str__(self):
        return self.brand


# Mikrotik Model
class Mikrotik(models.Model):
    choice_status = (('Active', 'Active'), ('Stored', 'Stored'), ('Damaged',
                                                                  'Damaged'))
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    pop_name = models.CharField(max_length=200)
    status = models.CharField(max_length=100,
                              choices=choice_status,
                              default='Active')
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model


# Olt Model
class Olt(models.Model):
    choice_status = (('Active', 'Active'), ('Stored', 'Stored'), ('Damaged',
                                                                  'Damaged'))
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200, unique=True)
    pon_ports = models.IntegerField()
    area = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=choice_status)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.area


# Onu Model


class Onu(models.Model):
    choice_status = (('Active', 'Active'), ('Stored', 'Stored'), ('Damaged',
                                                                  'Damaged'))
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200, unique=True)
    pon_mac = models.CharField(max_length=200, unique=True)
    ethernet_ports = models.IntegerField()
    status = models.CharField(max_length=100, choices=choice_status)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pon_mac


# Switch Model
class Switch(models.Model):
    choice_status = (('Active', 'Active'), ('Stored', 'Stored'), ('Damaged',
                                                                  'Damaged'))
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200, unique=True)
    ethernet_ports = models.IntegerField()
    status = models.CharField(max_length=100, choices=choice_status)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial_number


# Router Model
class Router(models.Model):
    choice_status = (('Active', 'Active'), ('Stored', 'Stored'), ('Damaged',
                                                                  'Damaged'))
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    mac = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=100, choices=choice_status)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mac
