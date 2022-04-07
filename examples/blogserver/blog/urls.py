from django.conf.urls import *

urlpatterns = ['blogserver.blog.views',
    url(r'^$', 'posts', name='posts'),
    url(r'^js$', 'test_js'),
]
