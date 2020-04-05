from django.db import models
# out of the box django comes with the default user model that is used with the standard authentication system and also the django admin
# we are going to override this with our custom module that allows to use an email address instead of the standar username that comes
# with standard django model. Below are the imports you need to add
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# under this we need to create a new class called user profile and inherit from AbstractUser and PermissionsMixin
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):# if you do not specify a password it will default to None and because of how django works a no password will not work you will not be able to authenticate with the user
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        #next we do whatis called normalizing an email address it does second half email address all lower case in order to have only one email address
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # this ensure that the password is always encrypted in the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new supersuer with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractUser, PermissionsMixin):
    """Database model for user in the system""" # python standard for writing docstrings
    email = models.EmailField(max_length=255, unique=True)
    # the above line email means we want an email column on our userprofile database and we want this column field filled with max 255 character and
    # unique= True means two users can not use same email address so each user is unique
    name = models.CharField(max_length=255)
    # the above allow 255 character for the name field
    is_active = models.BooleanField(default=True)
    # the above line is used to determine if a user is active or not - by default we set it to true
    is_staff = models.BooleanField(default=False)
    # the above determine if the user is a staff user which is used to determine if the user should have access to the django admin - in this case by default all user are not django admin
    objects = UserProfileManager()
    USERNAME_FIELD = 'email' # this allow to change from defaul username authentication to email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return  self.name

    def __str__(self):
        """Return string rappresentation of our user"""
        return self.email #reccomended for all django model

