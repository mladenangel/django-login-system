"""coin URL Configuration

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
from django.contrib import admin
from profiles import views as profiles_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls.static import static
from checkout import views as checkout_views
from . import views as root_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app.urls')),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    url(r'^checkout/$', checkout_views.checkout, name='checkout'),
    url(r'^chart/$', root_views.chart, name='chart'),

]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


