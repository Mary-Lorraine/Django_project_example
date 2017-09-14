from django.conf.urls import url
from . import views


# urls
urlpatterns = [
    url(r'^$', views.StockList.as_view(), name='viewresults'),
    url(r'stockdetails/$', views.StockDetails.as_view(), name='stockdetails'),
]
