from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}


urlpatterns = [
    '',
    url(r'^admin/', include(admin.site.urls)),

    # SEO API's
    url(
        r'^sitemap.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
