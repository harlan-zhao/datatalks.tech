from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import homepage,register,login,profile,redirecting,api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from autochart.views import upload,filecheck,visualization,checkbox


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='home'),
    path('upload/',upload),
    path('filecheck/',filecheck),
    path('filechoose/',checkbox),
    path('visualization/',visualization),
    path('register/',register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',profile,name='profile'),
    path('apiusage/',api,name='apiusage'),
    path('redirecting/',redirecting,name='redirecting'),
    path('',include('api.urls')),
]

urlpatterns += staticfiles_urlpatterns()