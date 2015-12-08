from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # SEO API's
    url(
        r'^sitemap.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}
    ),

    # webmaster verification
    url(r'^', include('webmaster_verification.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
