
from django.urls import path
from .views import ProductView,ProductDetailView,royalCanin,search_products,CategoryDetailView
from .views import ProductCreateView,ProductUpdateView,ProductDeleteView,ProductAdminView
urlpatterns = [

    path("products/",ProductView.as_view(),name="products"),
    path("products/<int:pk>",ProductDetailView.as_view(),name="productdetail"),
    path("products/royal-canin",royalCanin,name="royal_canin"),
    path("products/search",search_products,name="search"),
    path("category/<slug:slug>",CategoryDetailView.as_view(),name="category"),
    path("create-product/",ProductCreateView.as_view(),name="createProduct"),
    path("update-product/<int:pk>",ProductUpdateView.as_view(),name="updateProduct"),
    path("delete-product/<int:pk>/",ProductDeleteView.as_view(),name="delete-product"),
    path("product-admin/",ProductAdminView.as_view())

  
]
