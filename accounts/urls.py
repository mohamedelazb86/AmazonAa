from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('<str:username>/activate',views.activate_code,name='activate_code'),
]
