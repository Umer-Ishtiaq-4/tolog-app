
from django.urls import path, include
from customauthorization import views
urlpatterns = [
    
    path('login/', views.login_view, name='loginPage'),
    path('register/', views.register_view, name='registerPage'),
    path('logout/', views.logout_view, name='logoutPage'),
    
]