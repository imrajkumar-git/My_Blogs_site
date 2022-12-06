from django.urls import path
from main import views
from .views import searchdata
urlpatterns = [
    path('', views.blog_home, name="home"),
    path('blog_detail', views.blog_detail, name="blog_detail"),

    path('blog_detail/<str:slug>', views.blog_detail, name="blog_detail"),
    path('contact_us/', views.contactUs.as_view(), name="contact_us"),

    path('create_new_blog/', views.CreateBlog.as_view(), name="create-blog"),

    path('update_blog/<int:pk>/', views.UpdateBlogView.as_view(), name="UpdateBlogView"),

    path('delete_blog/<int:pk>/', views.DeleteBlogView.as_view(), name="DeleteBlogView"),
    path('home', searchdata, name="search")

]
