from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

handler404 = 'hello.views.handler404'
handler500 = 'hello.views.handler500'
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'call.html', hello.views.call, name='call'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
