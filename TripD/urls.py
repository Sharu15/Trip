# """myblog URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from Diaries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tripdiaries/', views.tripdiaries, name='tripdiaries'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
    path('new_post/', views.new_post, name='new_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('plan/', views.plan, name='plan'),
    path('', views.post_list, name='post_list'), 
    path('plan_list/', views.plan_list, name='plan_list'), 
    path('plan/<int:pk>/', views.plan_detail, name='plan_detail'),
    path('profile/', views.profile, name='profile'),

    # path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),  
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
   
]

    


    
    
   
    
   
#     