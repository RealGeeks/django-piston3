from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = ['',
    url(r'^', include('blogserver.blog.urls')),
    url(r'^api/', include('blogserver.api.urls')),
    url(r'^admin/(.*)', admin.site.root),
]
