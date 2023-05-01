from django.contrib import admin
from django.urls import path
from shopapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home),
    path('login',views.login),
    path('logout',views.logout),
    path('registration',views.registration),
    path('baseadmin',views.baseadmin),
    path('save_userdata',views.save_userdata),
    path('forget',views.forget),
    path('getlogin',views.getlogin),
    path('firstadd',views.firstadd),
    path('viewadmin',views.viewadmin),
    path('editadmin/<int:id>',views.editadmin),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changeedit/<int:id>',views.changeedit),
    path('product_save',views.product_save),
    path('search',views.search),
    path('productview/<int:id>',views.productview),
    path('buying',views.buying),
    path('addcart/<int:id>',views.addcart),
    path('view_addcart',views.view_addcart),
    path('addelete/<int:id>',views.addelete),
    # path('cartstore',views.cartstore),
  
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)