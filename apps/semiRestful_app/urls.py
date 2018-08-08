from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^add$', views.add),
    url(r'^user/(?P<userid>\d+)$', views.show),
    url(r'^user/(?P<userid>\d+)/edit$', views.edit),
    url(r'^(?P<userid>\d+)/edit$', views.edit),
    url(r'^update$', views.update),
    url(r'^user/(?P<userid>\d+)/delete$', views.destroy),
]