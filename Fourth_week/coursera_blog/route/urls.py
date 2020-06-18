from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^simple_route/$', ok),
    url(r'^slug_route/([0-9a-z_\-]{1,16})/$', slug_route),
    url(r'^sum_route/(-*\d+)/(-*\d+)/*$', sum),
    url(r'^sum_get_method/', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method),
]
