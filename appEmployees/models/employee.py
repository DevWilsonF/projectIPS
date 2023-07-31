from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class AdminUser (BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Los usuarios deben tener un username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):

        user = self.create_user(
            username = username,
            password = password
        )
        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=25, unique=True)
    password = models.CharField('Password', max_length=15)
    role = models.CharField('Role', max_length=30,null=False)
    state =models.BooleanField('Estado',default=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = AdminUser()
    USERNAME_FIELD = 'username'