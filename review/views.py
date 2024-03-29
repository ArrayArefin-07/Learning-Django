from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from.forms import BuildingAdd,ModifySuccessForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def customer(request):
    return render(request,'review/review.html')
# Registration
def building_form(request):
    if request.method == "POST":
        frm = BuildingAdd(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = BuildingAdd()  # Add parentheses to create an instance
    return render(request, 'review/building.html', {'form': frm})

# Login
def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data=request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data['username']
            userp = frm.cleaned_data['password']
            user = authenticate(username=usern, password=userp)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/rvw/success')
        else:
            # Return a response with the form in case of invalid input
            return render(request, 'review/login.html', {'form': frm})

    else:
        frm = AuthenticationForm()
        return render(request, 'review/login.html', {'form': frm})

# Successfully Login
def login_success(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = ModifySuccessForm(request.POST, instance =request.user)
            if frm.is_valid():
                frm.save()
        else:
            frm = ModifySuccessForm(instance = request.user)
        return render (request, 'review/success.html',{'form': frm})
    else:
        return HttpResponseRedirect('/login/')
    
        frm = ModifySuccessForm(instance = request.user)
        return render(request, 'review/success.html',{'form':frm})

# Logout
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/rvw/login')

#password change using old password
def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = PasswordChangeForm(user=request.user, data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/rvw/success')
        else:
            frm = PasswordChangeForm(user= request.user)
        return render(request, 'review/cpass.html', {'form': frm})
    else:
        return HttpResponseRedirect('/rvw/login')

#without old password
def change_pass_without_oldpass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = SetPasswordForm(user=request.user, data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/rvw/success')
        else:
            frm = PasswordChangeForm(user= request.user)
        return render(request, 'review/withoutoldpass.html', {'form': frm})
    else:
        return HttpResponseRedirect('/rvw/login')