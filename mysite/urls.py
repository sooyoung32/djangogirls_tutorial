from django.conf.urls import include, url
from django.contrib import admin

# urlresolver가 사용하는 패턴 목록을 저장함
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
