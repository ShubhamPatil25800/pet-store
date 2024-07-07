from django.urls import path
from . import views
urlpatterns = [

    path("add-to-cart/<int:productId>",views.add_to_cart,name="add-to-cart"),
    path("",views.view_cart,name="cart"),
    path("remove-from-cart/<int:cartItemId>",views.delete_cartitem,name="delete-cartitem"),
    path("update-quantity/<int:cartItemId>",views.update_quantity,name="update-quantity"),
    path("checkout/",views.checkout,name="checkout"),
    path("payment/<str:orderId>/",views.payment,name="payment"),
    path("success/<str:orderId>/",views.success,name="success")
    
]
