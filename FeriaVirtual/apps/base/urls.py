from django.urls import re_path as url, include
from apps.base.views import index

from django.urls import include, path

app_name = "base";

urlpatterns = [
url(r'^$', index,name='index'),
]