from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .import views


urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register_user'),
    path('token/', TokenObtainPairView.as_view(), name='Token'),
    path('refresh/', TokenRefreshView.as_view(), name='Refresh'),
    path('detail/', views.DetailsView.as_view(), name='detail_view'),
]