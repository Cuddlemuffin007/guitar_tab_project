"""guitar_tab_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tab_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index_view'),
    url(r'^results/$', views.SearchResultsView.as_view(), name='search_results_view'),
    url(r'^top_tabs/$', views.TopTabsView.as_view(), name='top_tabs_view'),
    url(r'^(?P<artist_url>tabs/\w/.+/)$', views.ArtistSongsView.as_view(), name='artist_song_list_view'),
    url(r'^(?P<url>.+)', views.TabView.as_view(), name='tab_detail_view')
]
