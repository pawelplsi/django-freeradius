from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # django_freeradius urls
    # keep the namespace argument unchanged
    # url(r'^', include('django_freeradius.urls', namespace='freeradius')),
]

urlpatterns += staticfiles_urlpatterns()
