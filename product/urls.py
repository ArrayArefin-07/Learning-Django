from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.product, name='productpage'),
    path("recent/",views.details),
    path("successfully/", views.send),
    path("middleware/", views.midd)

    
         
]
