from django.urls import path
from base.views import user_views as views
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),
    path('profile/', views.UserProfileAPIView.as_view(), name='profile'),
    path('profile/update/', views.UpdateUserProfileAPIView.as_view(), name='profile-update'),
    path('', views.GetUsersAPIView.as_view(), name='all_user'),
]
