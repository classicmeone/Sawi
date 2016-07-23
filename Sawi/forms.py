from django import forms
import re
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import * #Course, News
from _hashlib import new



class AuthUser(ModelForm):
    fields = {'username', 'firstname', 'lastname', 'email', 'is_active'}
    model = User
    

    
class Commons(forms.Form):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length = 30)
    sex = forms.CharField(max_length = 30)
    DOB = forms.DateField()
    address = forms.CharField(max_length=30)
    
    class Meta:
        abstract = True
class AdmissionForm(Commons):
    course = forms.CharField(max_length=30)
    
    
class Login(forms.Form):
    username = forms.CharField(max_length = 32,
                               required = True,
                               label = 'Username')
    password = forms.CharField(required = True,
                               label = 'Password',
                               max_length = 32,
                               widget = forms.PasswordInput())
    confirmPassword = forms.CharField(required = True,
                                      label='Confirm Password',
                                      max_length = 32,
                                      widget=forms.PasswordInput())


class UserReg(forms.Form):
    firstname = forms.CharField(max_length = 30, required=True, label = "Firstname")
    lastname = forms.CharField(max_length = 30,
                                required=True,
                                label = "Lastname",
                                )
    email = forms.EmailField(max_length = 30,
                            required =True,
                            label = "Email")
    password = forms.CharField(required = True,
                               label = 'Password',
                               max_length = 32,
                               widget = forms.PasswordInput())
    confirmPassword = forms.CharField( max_length = 32,
                                       required = True,
                                       widget= forms.PasswordInput())
    username = forms.CharField(max_length = 20, required= True)
    def clean_confirmPassword(self):

        if (password in self.clean_data) and (confirmPaasword in self.clean_data):
            pass1 = self.clean_data['password']
            pass2 = self.clean_data['confirmPassword']

            if pass1 == pass2:

                return pass2;
            else:
                self.add_error('confirmPassword', 'Password mismatch')
            raise forms.ValidationError('Password mismatch')
    def clean_username(self):
        username = self.clean_data['username'];
        if not re.search(r'^\w+$', username):

            raise forms.ValidationError("Alphanumeric not allowed for username");
        try:
            User.objects.get(username = username)
        except:
            return username
        raise forms.ValidationError("Duplicate username not allow")

class StudentReg(forms.Form):
    pass
class SearchForm(forms.Form):
    query = forms.CharField(
        label = "Enter to Search",
        required = True,
        widget = forms.TextInput(attrs = {'size':32}))
    
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 30, required = True);
    email = forms.EmailField(max_length = 30, required = True)
    comment = forms.CharField(required  = True, widget = forms.Textarea)

class CourseEdit(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'#['title', 'description', 'duration']


class FormsetTest(forms.Form):
     name = forms.CharField(max_length = 30, required = True);
     email = forms.EmailField(max_length = 30, required = True)
     comment = forms.CharField(required  = True, widget = forms.Textarea)
     
     
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title','brief','details']
        
class FileUpload(forms.Form):
    title = forms.CharField(max_length = 20, required=False)
    image = forms.FileField(label="Upload File")

    
    