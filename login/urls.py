from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from login import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('user/all/', views.APIObjects.as_view()),
    path('user/<int:pk>/', views.APIObjectsDetails.as_view()),
    path('', views.homepage, name = 'homepage'),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('user/',views.index, name = 'Loginview'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
