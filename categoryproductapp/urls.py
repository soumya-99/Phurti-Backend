from django.conf.urls import url
from categoryproductapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^category$', views.categoryAPI),
    # url(r'^category/([0-9]+)$', views.categoryAPI),
    url(r'^product$', views.productAPI),
    # url(r'^product/([0-9]+)$', views.productAPI),
]
