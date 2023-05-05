from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import customer
class CustomerRegistrationForm(UserCreationForm):
    email= forms.CharField(required=True, widget = forms.EmailInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label='Confirm Password (again) ', widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    
 
    class Meta:
        model = User
        fields = [ 'username','email','password1','password2']
        labels = {'email': "Email"}
        widgets = { 'username':forms.TextInput(attrs={'class': 'form-control'})}


class authentication(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'class': 'form-control','autofocus':True}))
    password = forms.CharField(label= "Password",widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class password_change(PasswordChangeForm):
    old_password = forms.CharField(label= "Old Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','autofocus': 'Ture',"class":'form-control'}))
    new_password1 = forms.CharField(label= "New Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','autofocus': 'Ture',"class":'form-control'}))
    new_password2  = forms.CharField(label= "Confirm New Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','autofocus': 'Ture',"class":'form-control'}))



class customerprofileform(forms.ModelForm):
    class Meta:
        model  = customer
        fields = ['name','main_address','street_address','additional_address','phone_number']
        # labels = {'additional_address' : "NAME"}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Home Office GF Home.....'}),
                   'main_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Bharatpur-2-LionsChowk'}),
                   'street_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Balkumari road'}),
                   'additional_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Nearby shops,hospitals,schools or other'}),
                   'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'9846xxxxxx'})}



class password_reset_form(PasswordResetForm):
    email= forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class': 'form-control','autocomplete':'email'}))

   
class password_set(SetPasswordForm):
    new_password1 = forms.CharField(label= "New Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','autofocus': 'Ture',"class":'form-control'}))
    new_password2  = forms.CharField(label= "Confirm New Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','autofocus': 'Ture',"class":'form-control'}))

