
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="shopHome"),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.contact, name="ContactUs"),
    path("search/",views.search, name="search"),
    path("products/<int:myid>",views.prodView, name="search"),
    path("checkout/",views.checkout, name="checkout")  
]

