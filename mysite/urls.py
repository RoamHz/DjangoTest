"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
#from mysite.views import hello, current_datetime, hours_ahead, contact
#from books import views
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^reviews/2003/$', views.special_case_2003),
    url(r'^reviews/([0-9]{4})/$', views.year_archive),
    url(r'^reviews/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^reviews/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.review_detail),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]