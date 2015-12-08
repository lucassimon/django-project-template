# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


# Third-party app imports

# Imports from your apps


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            # 'home',
            # 'lodges:lodge_listview',
            # 'organizers:organizer_listview',
            # 'contacts:contact-create',
            # 'schedules:schedule_listview'
        ]

    def location(self, item):
        return reverse(item)
