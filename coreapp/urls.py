from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.create_post, name='create_post'),
    path('blog/my_posts/', views.my_posts, name='my_posts'),
    path('blog/my_posts/<int:pk>/', views.my_post, name='my_post_view'),
    path('blog/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('blog/delete/<int:pk>/', views.delete_post, name='delete_post'),
]