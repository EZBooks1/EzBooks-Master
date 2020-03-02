###############################################################################
#                          Views for the ez_main app                          #
###############################################################################

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
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
   class_extensions = []   # Empty list used to store the class extensions
   book     = Books()      # Books object initialization
   user     = request.user # Get the currently authenticated user
   no_books = True         # Flag value, assuming no books exist for a user

   class1  = user.class_schedule.class1
   class2  = user.class_schedule.class2
   class3  = user.class_schedule.class3
   class4  = user.class_schedule.class4
   class5  = user.class_schedule.class5
   class6  = user.class_schedule.class6
   classes = Classes_list()
   display_classes = classes.display_classes(class1, class2, class3, class4, class5, class6)

   # Get all the class extensions
   for obj in display_classes:
      class_extensions.append(obj.class_extension)

   if request.POST:
      # Regenerate a schedule for the user on button click
      if 'regenerate' in request.POST:
         new_users_schedule = Class_schedule(user.id)
         new_users_schedule.create_class(user.major)
         new_users_schedule.save()
         Books.objects.filter(user_id__pk=user.id).delete()
         no_books = True
         return HttpResponseRedirect(reverse('ez_main:class_page'))
   
      # Get books for the user if they have none on button click
      if 'confirm' in request.POST:
         for book in Books.objects.filter(user_id__pk=user.id)[:1]:
            no_books = False
         if no_books:
            book = book.find_books(class_extensions, user)
         return HttpResponseRedirect(reverse('ez_main:books_page'))

   return render(request, 'ez_main/class_page.html', {'display_classes': display_classes})

@login_required
def books_page(request):
   """ Return the users needed textbooks page """
   user_books = []           # Create an empty list for the users books
   user       = request.user # Get the currently authenticated user

   for book in Books.objects.filter(user_id__pk=user.id):
      user_books.append(book)

   # Delete books from the users list of books on button click
   if request.POST:
      for book in user_books:
         if str(book.id) in request.POST:
            Books.objects.filter(id=book.id).delete()
            break
      return HttpResponseRedirect(reverse('ez_main:books_page'))

   return render(request, 'ez_main/books_page.html', {'user_books': user_books})

@login_required
def checkout_summary(request):
   """ Return a summary of the books being ordered by the user """
   user_books = []           # List of the users books which they are trying to buy
   user       = request.user # Get the currently authenticated user

   for book in Books.objects.filter(user_id__pk=user.id):
      user_books.append(book)

   return render(request, 'ez_main/checkout_summary.html', {'user_books': user_books})

@login_required
def checkout_page(request):
   """ Return the page to collect purchase information from the user """
   return render(request, 'ez_main/checkout_page.html')