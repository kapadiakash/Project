# We are in urls.py file of core app

from django.urls import path
from . import views
#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------------------
urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name='home'),

    path('about/',views.about,name='about'),

    path('contact/',views.contact,name='contact'),

    #------- scooty View Functions ------------
    # path('scooty_superegories',views.scooty_superegories,name='scootysuperegories'),
    path('scooty_superegories/',views.scootysuperegoriesView.as_view(),name='scootysuperegories'),

    #------- super View Functions ------------
    # path('super_superegories',views.super_superegories,name='supersuperegories'),
    path('super_superegories/',views.supersuperegoriesView.as_view(),name='supersuperegories'),

    #------- bike View Functions ------------
    path('bike_superegories/',views.bike_superegories,name='bikesuperegories'),

    
    # path('Automobile_details',views.Automobile_details,name='Automobiledetails'),
    path('Automobile_details/<int:id>/',views.AutomobileDetailView.as_view(),name='Automobiledetails'),

    path('registration/',views.registration,name='registration'),

    path('login/',views.log_in,name='login'),

    path('profile/',views.profile,name='profile'),

    path('address/',views.address,name='address'),

    path('delete_address/<int:id>',views.delete_address,name='deleteaddress'),

    path('logout/',views.log_out, name="logout"),

    path('changepassword/',views.changepassword, name="changepassword"),

    path('add_to_cart/<int:id>/',views.add_to_cart, name="addtocart"),

    path('view_cart/',views.view_cart, name="viewcart"),

    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),

    path('delete_quantity/<int:id>/', views.delete_quantity, name='delete_quantity'),

    path('delete_cart/<int:id>',views.delete_cart, name="deletecart"),
    
    path('checkout/',views.checkout,name='checkout'),

]

#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)