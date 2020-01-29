###############################################################################
#                          Views for the ez_main app                          #
###############################################################################

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Classes_list

def home_page(request):
   """ Return the home page for ez_main """
   return render(request, 'ez_main/home_page.html')

def about_page(request):
   """ Return the about page for ez_main """
   return render(request, 'ez_main/about_page.html')

@login_required
def class_page(request):
   """ Return the users class schedule page """
   user    = request.user
   class1  = user.class_schedule.class1
   class2  = user.class_schedule.class2
   class3  = user.class_schedule.class3
   class4  = user.class_schedule.class4
   class5  = user.class_schedule.class5
   class6  = user.class_schedule.class6
   classes = Classes_list()
   display_classes = classes.display_classes(class1, class2, class3, class4, class5, class6)

   return render(request, 'ez_main/class_page.html', {'display_classes': display_classes})