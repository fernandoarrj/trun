from django.urls import path

from user import views

urlpatterns = [
    path('token/', views.UserTokenObtainKeyView.as_view()),
]
