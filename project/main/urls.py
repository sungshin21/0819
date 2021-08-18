from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include


from . import views
from main import views
from main.views import HomeView
from main.views import UserCreateView, UserCreateDoneTV


urlpatterns = [
    path('', views.main),
    path('/seoul', views.seoul ),
     path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    # path('login/', include('django.contrib.auth.urls')),
    path('login/', views.LoginView.as_view(), name="login"),
    
    path('signup/', UserCreateView.as_view(), name='register'),
    path('singup/done/', UserCreateDoneTV.as_view(), name='register_done'),
    # path('post/<int:pk>/', views.local_detail, name='local_detail'),

]