from django.urls import path
from . import views


urlpatterns = [
        # path('customers/', views.CustomerList.as_view()),
    # path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    # path('customer-change-password/<int:customer_id>/',
    #      views.CustomerChangePassword),
    # path('user/<int:pk>/', views.UserDetail.as_view()),
    path('customer/login/', views.customer_login, name='customer_login'),
    path('customer/register/', views.customer_register, name='customer_register'),
    # path('customer/<int:pk>/wishitems/',
    #      views.CustomerWishItemList.as_view()),
    # path('customer/<int:pk>/address-list/',
    #      views.CustomerAddressItemList.as_view()),

    
    path('products/', views.ProductList.as_view()),
    # path('products/<str:tag>', views.TagProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    # path('related-products/<int:pk>/', views.RelatedProductList.as_view()),
    # path('product-imgs/', views.ProducImgstList.as_view()),
    # path('product-imgs/<int:product_id>/', views.ProducImgstDetail.as_view()),
    # path('product-img/<int:pk>/', views.ProducImgtDetail.as_view()),
]
