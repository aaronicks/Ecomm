from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>/', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
] 

