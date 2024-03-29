# from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from product.forms import RecentProduct
from.models import laptop

# Create your views here.
def product(request):
    return render(request,'product/product.html')

def send(request):
    return render(request,'product/submit.html')
    

def details(request):
    if request.method =='POST':
        frm = RecentProduct(request.POST)
        if frm.is_valid():

            
            pas = frm.cleaned_data['password']
            rpas= frm.cleaned_data['re_password']
            lap= frm.cleaned_data['laptop']
            rlap = frm.cleaned_data['re_laptop']
            eml = frm.cleaned_data['email']
            abt = frm.cleaned_data['about']
            txt = frm.cleaned_data['textarea']
            chk = frm.cleaned_data['checkbox']
            rm = frm.cleaned_data['ram']
            ss = frm.cleaned_data['ssd']
            yt = frm.cleaned_data['youtube_chanel']
            buy = laptop(password = pas, re_password = rpas, laptop=lap,
            re_laptop=rlap, email=eml, about=abt, textarea=txt,checkbox=chk,
            ram=rm,ssd=ss,youtube_chanel=yt)
            buy.save()
            # print('youtube_chanel',frm.cleaned_data['youtube_chanel'])
            return HttpResponseRedirect('/pdc/successfully')

            
            #this portion for print input data at cmd/terminal
            # print('Valid form')
            # print('password :',frm.cleaned_data['password'])
            # print('re_password :',frm.cleaned_data['re_password'])
            # print('laptop :',frm.cleaned_data['laptop'])
            # print('re_laptop :',frm.cleaned_data['re_laptop'])
            # print('email :',frm.cleaned_data['email'])
            # print('about',frm.cleaned_data['about'])
            # print('textarea',frm.cleaned_data['textarea'])
            # print('checkbox',frm.cleaned_data['checkbox'])
            # print('ram',frm.cleaned_data['ram'])
            # print('ssd',frm.cleaned_data['ssd'])
            # print('youtube_chanel',frm.cleaned_data['youtube_chanel'])
            # return HttpResponseRedirect('/pdc/successfully')
        else:
            print('Invalid form:', frm.errors)

    else:
        frm = RecentProduct(auto_id=True, label_suffix=" ")
        print('GET Statement')
    
    return render(request,'product/recent.html',{'form':frm})

def midd(request):
    print("1st middleware")
    return HttpResponse("This is 1st middleware")
    