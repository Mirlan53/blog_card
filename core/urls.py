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
<<<<<<< HEAD
from blogs.views import blogs_index, user_page, friend_page, first_page, piramyda_page, kolizey_page, ploshad_page, efeleva_page, reykhstag_page, petergov_page, luvr_page, kreml_page, second_page, third_page, fourth_page, khram_page, tadzh_makhal_page, big_ben_page, statuya_page, machu_pikchu_page, fort_boyard_page, notr_dam_page, kitayskaya_stena_page 
=======
from blogs.views import blogs_index, user_page, friend_page, first_page, piramyda_page, kolizey_page, ploshad_page, efeleva_page, reykhstag_page, petergov_page, luvr_page, kreml_page
>>>>>>> 54e7d8fd22b43bf5e8f31c1208bf24ad93721ef2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('blogs', blogs_index, name='blogs_index'),
    path('user', user_page, name='user_page'),
    path('friend', friend_page, name='friend_page'),
    path('', first_page, name='first_page'),
=======
    path('', blogs_index, name='blogs_index'),
    path('user', user_page, name='user_page'),
    path('friend', friend_page, name='friend_page'),
    path('blog_list', first_page, name='first_page'),
>>>>>>> 54e7d8fd22b43bf5e8f31c1208bf24ad93721ef2
    path('piramyda', piramyda_page, name='piramyda_page'),
    path('kolizey', kolizey_page, name='kolizey_page'),
    path('ploshad', ploshad_page, name='ploshad_page'),
    path('efeleva', efeleva_page, name='efeleva_page'),
    path('reykhstag', reykhstag_page, name='reykhstag_page'),
    path('petergov', petergov_page, name='petergov_page'),
    path('luvr', luvr_page, name='luvr_page'),
    path('kreml', kreml_page, name='kreml_page'),
<<<<<<< HEAD
    path('second', second_page, name='second_page'),
    path('khram', khram_page, name='khram_page'),
    path('tadzh_makhal', tadzh_makhal_page, name='tadzh_makhal_page'),
    path('big_ben', big_ben_page, name='big_ben_page'),
    path('statuya', statuya_page, name='statuya_page'),
    path('machu_pikchu', machu_pikchu_page, name='machu_pikchu_page'),
    path('fort_boyard', fort_boyard_page, name='fort_boyard_page'),
    path('notr_dam', notr_dam_page, name='notr_dam_page'),
    path('kitayskaya_stena', kitayskaya_stena_page, name='kitayskaya_stena_page'),
    path('third', third_page, name='third_page'),
    path('fourth', fourth_page, name='fourth_page'),
=======
>>>>>>> 54e7d8fd22b43bf5e8f31c1208bf24ad93721ef2
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)