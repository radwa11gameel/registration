from django.urls import path
from products import views
from .api import ProductApi
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('product/<int:id>',views.detail,name='detail'),
    path('email/<int:id>',views.email,name='email'),
    path('api/v2/product/<int:pk>', ProductApi.as_view(), name='api'),

]