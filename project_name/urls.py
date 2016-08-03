from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # SEO API's
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
