from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    '',
    url(r'api/', include('test_project.apps.testapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
