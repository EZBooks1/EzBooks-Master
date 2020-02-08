###############################################################################
#                          Views for the ez_main app                          #
###############################################################################

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

def home_page(request):
   """ Return the home page for ez_main """
   return render(request, 'ez_main/home_page.html')

def about_page(request):
   """ Return the about page for ez_main """
   return render(request, 'ez_main/about_page.html')

@login_required
def class_page(request):
   """ Return the users class schedule page """
   array1 = [1,2,3,4,5,6]
   count = 0
   book  = Books()
   user    = request.user
   class1  = user.class_schedule.class1
   class2  = user.class_schedule.class2
   class3  = user.class_schedule.class3
   class4  = user.class_schedule.class4
   class5  = user.class_schedule.class5
   class6  = user.class_schedule.class6
   classes = Classes_list()
   display_classes = classes.display_classes(class1, class2, class3, class4, class5, class6)
   for obj in display_classes:
      a = obj.class_extension
      array1[count]=a
      count+=1
   count = 0

   for x in range(6):
      book = book.find_books(array1[count], user)
      count+=1

   return render(request, 'ez_main/class_page.html', {'display_classes': display_classes})

@login_required
def books_page(request):
   """ Return the users needed textbooks page """
   user_books = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
   user  = request.user
   count = 0
   for z in Books.objects.filter(user_id__pk=user.id):
      user_books[count] = z
      count+=1

   return render(request, 'ez_main/books_page.html', {'user_books': user_books})