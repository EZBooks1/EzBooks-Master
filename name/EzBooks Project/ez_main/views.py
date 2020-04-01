###############################################################################
#                          Views for the ez_main app                          #
###############################################################################

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
import users

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
   class_extensions = []   # Empty list used to store the class extensions
   book     = Books()      # Books object initialization
   user     = request.user # Get the currently authenticated user
    
   for book in Books.objects.filter(user_id__pk=user.id):
      user_books.append(book)

   # Delete books from the users list of books on button click
   if 'delete' in request.POST:
      Books.objects.filter(id=request.POST.get('delete')).delete()
      return HttpResponseRedirect(reverse('ez_main:books_page'))
   if 'undo_delete' in request.POST:
      classes = Classes_list()
      display_classes = classes.display_classes(user.class_schedule.class1, user.class_schedule.class2, user.class_schedule.class3, user.class_schedule.class4, user.class_schedule.class5, user.class_schedule.class6)
      Books.objects.filter(user_id__pk=user.id).delete()
      for obj in display_classes:
         class_extensions.append(obj.class_extension)
      book = book.find_books(class_extensions, user)
      
   return render(request, 'ez_main/books_page.html', {'user_books': user_books})

# @login_required
def checkout_summary(request):
   """ Return a summary of the books being ordered by the user """
   user_books = []           # List of the users books which they are trying to buy
   user       = request.user # Get the currently authenticated user

   for book in Books.objects.filter(user_id__pk=user.id):
      user_books.append(book)

   if request.POST:
      context = {'book_total': request.POST.get('total')}
      return render(request, 'ez_main/checkout_page.html', context)

   return render(request, 'ez_main/checkout_summary.html', {'user_books': user_books})

# @login_required
def checkout_page(request):
   """ Return the page to collect purchase information from the user """

   # Gather the information to send to the confirmation page
   if request.POST:
      context = {'fName': request.POST.get('fName'),
         'lName': request.POST.get('lName'),
         'dormChoice': request.POST.get('dormChoice'),
         'roomNum': request.POST.get('roomNum'),
         'bookTotal': request.POST.get('bookTotal')}
      return render(request, 'ez_main/confirmation_page.html', context)

   return render(request, 'ez_main/checkout_page.html')

# @login_required
def confirmation_page(request):
   """ Return the final confirmation of the users book order """
   user = request.user

   # Delete the users current books and log the user out
   if request.POST:
      Books.objects.filter(user_id__pk=user.id).delete()
      return users.views.logout(request)
   
   return render(request, 'ez_main/confirmation_page.html')

def guest_login(request):
   """ Login page for guests only """
   message = ""

   # Try to find the id of the user being searched on
   if request.POST:
      print(request.POST)
      username = request.POST.get('username')
      obj = User_profile.objects.raw("select id from main_db.users_user_profile where username = %s limit 1", [username])
      if obj:
         user = obj[0]
         print(user.id)
      else:
         message = "We were not able to find the user you are looking for, please try again"

   context = {'error_message': message}

   return render(request, 'ez_main/guest_login.html', context)

def contactinfo_page(request):
   """ Return the contact info page"""
   return render(request, 'ez_main/contactinfo_page.html')
