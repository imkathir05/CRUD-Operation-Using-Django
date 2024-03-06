
from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('updatedata/<int:id>', views.updatedata,name='updatedata'),
    path('deletedata/<int:id>', views.deletedata,name='deletedata'),
    
]
