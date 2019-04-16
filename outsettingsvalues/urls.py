from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BaseView.as_view(), name='base'),
    url(r'^/(?P<setting_name>\w+)/$', views.BaseView.as_view(), name='base')
]
