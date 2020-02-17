###############################################################################
#                          Models for the users app                           #
###############################################################################

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User_profile_manager(BaseUserManager):
   """ Manage the creation of the users profile """
   def create_user(self, username, major, password=None):
      """ Creates and saves a User with the required information """
      if not username:
         raise ValueError('Users must enter a valid username')
      user = self.model( username=username, major=major,)

      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, username, major, password):
      """ Create a user with admin priviledges """
      user = self.create_user(username, major, password=password,)
      user.is_admin = True
      user.save(using=self._db)
      return user

class User_profile(AbstractBaseUser):
   """ Model for the custom user profile """
   username = models.CharField(max_length=40, unique=True)
   major = models.CharField(max_length=100, default='Undecided')

   is_active = models.BooleanField(default=True)
   is_admin  = models.BooleanField(default=False)

   objects = User_profile_manager()

   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['major']

   def __str__(self):
      """ String representation of the model """
      return self.username

   def has_perm(self, perm, obj=None):
      """ Does the user have specific permissions? """
      return True

   def has_module_perms(self, users):
      """ Does user have permission to view user app content """
      return True

   @property
   def is_staff(self):
      """ Is the user a staff/admin member """
      return self.is_admin