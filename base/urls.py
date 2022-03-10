
from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
     path('home/', views.home, name="home"),
     path('about/', views.about, name="about"),
     path('files/', views.files, name="files"),
     path('login/', views.login_archma_api),
     path('user/', views.get_user_data),
     # path('register/', views.register_api),
     path('registers/',views.RegisterArchmaApiView.as_view()),
     path('logout/', knox_views.LogoutView.as_view()),
     path('UserList/', views.ArchmaUserList.as_view()),
     path('update/<str:pk>/', views.ArchmaUpdateUser.as_view()),
     path('logoutall/', knox_views.LogoutAllView.as_view())
]
