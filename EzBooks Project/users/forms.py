###############################################################################
#                           Forms for the users app                           #
###############################################################################

from django import forms
from .models import User_profile

# List of majors stored as a tuple
MAJORS= [

   ('Accounting', 'Accounting'),
   ('Advertising and Public Relations', 'Advertising and Public Relations'),
   ('Bible: General Studies', 'Bible: General Studies'),
   ('Biology', 'Biology'),
   ('Biology Education', 'Biology Education'),              
   ('Chemistry', 'Chemistry'),
   ('Computer Information Systems', 'Computer Information Systems'),
   ('Criminal Justice', 'Criminal Justice'),
   ('Cybersecurity', 'Cybersecurity'),
   ('Early Childhood Education', 'Early Childhood Education'),
   ('Electrical Engineering', 'Electrical Engineering'),
   ('Elementary Education', 'Elementary Education'),
   ('English', 'English'),
   ('English Education', 'English Education'),
   ('Finance', 'Finance'),
   ('Graphic Design', 'Graphic Design'),
   ('History', 'History'),
   ('History Education', 'History Education'),
   ('Humanities', 'Humanities'),
   ('Legal Office Administration', 'Legal Office Administration'),
   ('Legal Office Systems', 'Legal Office Systems'),
   ('Management', 'Management'),
   ('Marketing', 'Marketing'),
   ('Math Education', 'Math Education'),
   ('Mathematics', 'Mathematics'),
   ('Mechanical Engineering', 'Mechanical Engineering'),
   ('Medical Office Administration', 'Medical Office Administration'),
   ('Medical Office Systems', 'Medical Office Systems'),
   ('Missions', 'Missions'),
   ('Music', 'Music'),
   ('Music Education', 'Music Education'),
   ('Music Ministries', 'Music Ministries'),
   ('Nursing', 'Nursing'),
   ('Office Administration', 'Office Administration'),
   ('Office Systems', 'Office Systems'),
   ('Pastoral Ministries', 'Pastoral Ministries'),
   ('Performance Studies', 'Performance Studies'),
   ('Physical Education', 'Physical Education'),
   ('Political Science', 'Political Science'),
   ('Pre-Law', 'Pre-Law'),
   ('Pre-Medicine', 'Pre-Medicine'),
   ('Pre-Pharmacy', 'Pre-Pharmacy'),
   ('Pre-Physical Therapy', 'Pre-Physical Therapy'),
   ('Professional Writing', 'Professional Writing'),
   ('Science Education', 'Science Education'),
   ('Speech Education', 'Speech Education'),
   ('Sport Management', 'Sport Management'),
   ('Studio Art', 'Studio Art'),
   ('Youth Ministries', 'Youth Ministries')
   ]

class User_profileForm(forms.ModelForm):
   """Form to place data into the user profile model"""

   username  = forms.CharField(error_messages={'unique': 'This username is already taken, please choose something different.'})
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
   major     = forms.CharField(label='Major', widget=forms.Select(choices=MAJORS))

   class Meta:
      model = User_profile
      fields = ('username', 'major')

   def clean_password2(self):
      # Check that the two password entries match and that they are long enough
      password1 = self.cleaned_data.get("password1")
      password2 = self.cleaned_data.get("password2")
      if password1 and password2 and password1 != password2:
         raise forms.ValidationError("Passwords don't match")
      if len(password1) < 5:
         raise forms.ValidationError("Passwords must be at least 5 characters long")
      return password2

   def save(self, commit=True):
      # Save the provided password in hashed format
      user = super().save(commit=False)
      user.set_password(self.cleaned_data["password1"])
      if commit:
         user.save()
      return user