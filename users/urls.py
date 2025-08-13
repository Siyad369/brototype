from django.urls import path

from users import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout')
]
