
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('tem/',views.name)
    # path('bk',views.bkash),
    # path('math', views.add),
    # path('f', views.format),
    # path('uni',views.university),
    # path('pd', views.cake),
    # path('cr', views.customer)
    path('bkash/', views.bk , name='paymentone'),
    path('rocket/', views.rk, name='paymenttwo'), 
    path("pays/", views.payment_method),
    path("fv/", views.func_view),
    path("cv/", views.cls_view.as_view()),
    # path('tv/', views.FirstTV.as_view())
    path('tv/', views.TemplateView.as_view(template_name = 'payments/payments-1.html')),
    path('rv/', views.RedirectView.as_view(url = '/pay/tv')),
    path("ext/", views.externalRedirect.as_view())
    # path('product/', views.product, name='product'),
    # path('review/', views.review, name='review'),
         
]
