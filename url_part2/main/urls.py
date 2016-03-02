from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from main import views


urlpatterns = [
    url(r'^converter/$', login_required(views.Converter.as_view()), name='converter'),
    url(r'^url_list/$', login_required(views.URLList.as_view()), name='url_list'),
    url(r'^url_list/(?P<pk>\d+)/$', login_required(views.URLDetail.as_view()), name='url_detail'),
    url(r'^update_url/(?P<pk>\d+)/$', login_required(views.UpdateURL.as_view()), name='update_url'),
    url(r'^b/(?P<url>\w+)/$', login_required(views.URLRedirect.as_view()), name='url_redirect'),
]
