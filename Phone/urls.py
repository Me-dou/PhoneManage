from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneListCreate.as_view(), name='phone_list'),
    path('phone/<int:pk>/', views.PhoneRetrieveUpdateDelete.as_view(), name='phone_details'),
    path('categories/', views.CategoryListCreate.as_view(), name='Category_list'),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDelete.as_view(), name='category_detail'),
]

