from django.shortcuts import render
from payments.models import pay_method
from django.views import View
from django.views.generic.base import TemplateView,RedirectView
#from datetime import datetime

# Create your views here.
def bk(request):
    # d = datetime.now()
    # payment_method = 'Bkash'
    # Discount = '50%'
    # condition = 'Only first payment'
    # payments_details = {'pm':payment_method, 'dis':Discount}
    # names ={'friends':['sohan','shakil','imran','sehab','plabon','sakib']}
    return render(request, 'payments/payments-1.html')
    
def rk(request):
    return render(request, 'payments/payments-2.html')

def payment_method(request):
    pay_m= pay_method.objects.all()
    return render(request, 'payments/pay.html',{'pay': pay_m})

#Function based view
def func_view(request):
    return render (request, 'product/product.html')

#Class based View
class cls_view(View):
    def get(self,request):
        return render(request,'product/product.html')
        

#TemplateView
# class FirstTV(TemplateView):
#     template_name = 'payments/payments-1.html'
    
#Redirect View
class externalRedirect(RedirectView):
    url= 'https://www.youtube.com/@m-arefinsuniverse1486'
    
#custom 404 view 
# def custom_404(request, exception):
#     return render(request, 'templates/payments/404.html', status=404)