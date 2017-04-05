"""ombudsman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^auth/v1/$', views.validate_auth, name='validate_auth'),
    url(r'^reviews/v1/(?P<app_store_id>[\w\.]+)/$', views.reviews, name='reviews'),
    url(r'^acquisitions/v1/(?P<app_store_id>[\w\.]+)/$', views.acquisitions, name='acquisitions'),
    url(r'^add-on-acquisitions/v1/(?P<app_store_id>[\w\.]+)/$', views.add_on_acquisitions, name='add_on_acquisitions'),
    url(r'^installs/v1/(?P<app_store_id>[\w\.]+)/$', views.installs, name='installs'),
    url(r'^ratings/v1/(?P<app_store_id>[\w\.]+)/$', views.ratings, name='ratings'),
    url(r'^ads-performance/v1/(?P<app_store_id>[\w\.]+)/$', views.ads_performance, name='ads_performance'),
    url(r'^ad-campaign-performance/v1/(?P<app_store_id>[\w\.]+)/$', views.ad_campaign_performance, name='ad_campaign_performance'),
    url(r'^errors/v1/(?P<app_store_id>[\w\.]+)/$', views.errors, name='errors'),

    url(r'^admin/', admin.site.urls),
]
