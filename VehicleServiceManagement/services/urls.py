from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   # path('login/', auth_views.LoginView.as_view(), name='login'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('add_service/<int:vehicle_id>/', views.add_service, name='add_service'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('profile/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
