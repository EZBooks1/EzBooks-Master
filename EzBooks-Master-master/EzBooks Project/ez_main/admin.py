###############################################################################
#                  Registrations for the ez_main app models                   #
###############################################################################

from django.contrib import admin
from .models import *

admin.site.register(Classes_list)
admin.site.register(Class_schedule)
admin.site.register(Book_list)
admin.site.register(Books)