###############################################################################
#                    Registrations for the user app models                    #
###############################################################################

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import User_profileForm
from .models import User_profile

admin.site.register(User_profile)