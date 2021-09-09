from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',views.home,name='home'),
    path('transfer/',views.Transfer,name='transfer'),
    path('customers/',views.Customers,name='customers'),
    path('register/',views.register,name='register'),
    path('transaction/',views.Transaction,name='transaction'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact')

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)