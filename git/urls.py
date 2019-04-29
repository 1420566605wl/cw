from django.conf.urls import url
from django.contrib import admin
from web.views import ShowView,AddView,DelView,UpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ShowView/', ShowView.as_view(),name='show'),
    url(r'^AddView/', AddView.as_view(),name='add'),
    url(r'^DelView/(\d+)/', DelView,name='del'),
    url(r'^UpdateView/(\d+)/', UpdateView.as_view(),name='update'),
]
