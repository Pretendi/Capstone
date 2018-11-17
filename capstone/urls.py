"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls    import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from account import views as account_views
from service import views as service_views

"""
urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^account/', include('account.urls')),
    # url(r'^service/', include('service.urls')),
    url(r'^admin/', admin.site.urls),
]
"""

urlpatterns = [
    path('', views.home, name = 'webapp-home'),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login_paul.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_paul.html'), name='logout'),
    path('survey/', account_views.survey, name='survey'),
    path('select/', service_views.select, name='select'),
    path('admin/', admin.site.urls),
]
 
 #      {% if messages %}
 #           {% for message in messages %}
 #               <div class="alert alert-{{ messages.tags }}">
 #                   {{ message }}
 #              </div>
 #           {% endfor }
 #       {% endif %}
