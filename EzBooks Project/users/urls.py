###############################################################################
#                       Url Patterns for the users app                        #
###############################################################################

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
   # Login path
   path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

   # Register path
   path('register/', views.register, name='register'),

   # Logout path
   path('logout/', views.logout, name='logout'),
]