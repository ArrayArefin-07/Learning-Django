from django.core import validators
from django import forms

class RecentProduct(forms.Form):
    password= forms.CharField(widget=forms.PasswordInput)
    re_password= forms.CharField(widget=forms.PasswordInput)
    laptop= forms.CharField(label='Enter your laptop Name')
    re_laptop= forms.CharField(label='Enter your confirm laptop Name')
    #form Validation using validators at email
    email = forms.EmailField(initial="mobasherarefint2001@gmail.com",label_suffix='=',validators=[validators.MaxLengthValidator(20)])
    about=forms.CharField(help_text="Describe about laptop")
    textarea= forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols': 40}))
    checkbox= forms.CharField(widget=forms.CheckboxInput)
    # files = forms.CharField(widget=forms.FileInput) 
    ram= forms.IntegerField(min_value=4,max_value=12)
    ssd = forms.DecimalField(min_value=1,max_value=50, max_digits=3,decimal_places=2)
    youtube_chanel=forms.BooleanField(label='Subscribe the youtube Channel')

    def clean(self):
        cleaned_data= super().clean()
        password_match= self.cleaned_data['password']
        re_password_match= self.cleaned_data['re_password']
        if password_match != re_password_match:
            raise forms.ValidationError("Password dosen't match")
        
    def clean(self):
        cleaned_data= super().clean()
        laptop_match = self.cleaned_data["laptop"]
        re_laptop_match= self.cleaned_data['re_laptop']
        if laptop_match != re_laptop_match:
            raise forms.ValidationError("Laptop Name dosen't Match")

        

#form Validation using CleanMethod
    # def clean_password(self):
    #     password_validation = self.cleaned_data['password']
    #     if len(password_validation)<4:
    #         raise forms.ValidationError("Enter Your Correct Password")
    #     return password_validation
        
    # def clean_laptop(self):
    #     laptop_validation = self.cleaned_data['laptop']
    #     if len(laptop_validation)<10:
    #         raise forms.ValidationError("Enter Correct Format")
    #     return laptop_validation

