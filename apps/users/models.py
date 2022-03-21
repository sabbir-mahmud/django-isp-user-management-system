# imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

# user manager


class UserManager(BaseUserManager):
    # create user
    def create_user(self, user_id, password=None):
        if not user_id:
            raise ValueError('Enter a valid user_id')

        user = self.model(user_id=user_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create super user / admin
    def create_superuser(self, user_id, password=None):
        if not user_id:
            raise ValueError('Enter a valid user_id')

        user = self.model(user_id=user_id)
        user.set_password(password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# user id model


class UserId(models.Model):
    user = models.IntegerField(default=1000)

    def __str__(self):
        return str(self.user)

# user model


class User(AbstractBaseUser):
    user_id = models.IntegerField(unique=True,)
    client = models.BooleanField(default=True)
    reseller = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    worker = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    # username replaced with user_id
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return str(self.user_id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.staff == True:
            return True
        else:
            return False

    @property
    def is_superuser(self):
        if self.admin == True:
            return True
        else:
            return False


# owner model
class Owners(models.Model):
    choice_status = (('Active', 'Active'), ('Inactive', 'Inactive'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=245, choices=choice_status)
    address = models.CharField(max_length=245)
    invest_amount = models.FloatField(default=0)
    commission = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.user_id)

# staff id model


class Staff_Id(models.Model):
    staff_id = models.IntegerField(unique=True, default=20113)

    def __str__(self):
        return str(self.staff_id)

# staff model


class Staffs(models.Model):
    choice_status = (('Active', 'Active'), ('Inactive', 'Inactive'))
    stafftype = (('Owner', 'Owner'),
                 ('Accountant', 'Accountant'),
                 ('Server Team', 'Server Team'),
                 ('Fiber Team', 'Fiber Team'),
                 ('Support Team', 'Support Team'),
                 ('Sales Team', 'Sales Team'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staffs_Id = models.ForeignKey(
        Staff_Id, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=245)
    salary = models.FloatField(default=0)
    stafftype = models.CharField(max_length=245, choices=stafftype)
    status = models.CharField(max_length=245, choices=choice_status)

    def __str__(self):
        return str(self.staffs_Id)
