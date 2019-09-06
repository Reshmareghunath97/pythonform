from django.urls import path
from . import views
urlpatterns = [
   path('', views.registration, name='registration'),
   path('signin/', views.signin, name='signin'),
   path('end/', views.end, name='end'),
   path('logout/', views.logout_view, name='logout'),
   path('admin_home/', views.admin_view, name='admin'),
   path('edit/<int:id>/', views.edit, name='edit')
   ]