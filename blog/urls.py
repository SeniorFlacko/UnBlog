from django.conf.urls import url
from . import views
from . import feed

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
]