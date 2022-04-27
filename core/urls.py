"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs.views import blogs_index, user_page, friend_page, first_page, piramyda_page, kolizey_page, ploshad_page, efeleva_page, reykhstag_page, petergov_page, luvr_page, kreml_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogs_index, name='blogs_index'),
    path('user', user_page, name='user_page'),
    path('friend', friend_page, name='friend_page'),
    path('first', first_page, name='first_page'),
    path('piramyda', piramyda_page, name='piramyda_page'),
    path('kolizey', kolizey_page, name='kolizey_page'),
    path('ploshad', ploshad_page, name='ploshad_page'),
    path('efeleva', efeleva_page, name='efeleva_page'),
    path('reykhstag', reykhstag_page, name='reykhstag_page'),
    path('petergov', petergov_page, name='petergov_page'),
    path('luvr', luvr_page, name='luvr_page'),
    path('kreml', kreml_page, name='kreml_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)