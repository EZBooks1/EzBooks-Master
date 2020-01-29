###############################################################################
#                      Url Patterns for the ez_main app                       #
###############################################################################

from django.urls import path

from . import views

# Url patterns for the ez_main app
app_name = 'ez_main'
urlpatterns = [
   # Home page path
   path('', views.home_page, name='home_page'),

   # About page path
   path('about/', views.about_page, name='about_page'),

   # Class page path
   path('class/', views.class_page, name='class_page'),

   # Book page path
   path('books/', views.books_page, name='books_page'),
]