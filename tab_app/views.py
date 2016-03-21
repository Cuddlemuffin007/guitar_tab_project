from django.views.generic import TemplateView
from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://www.guitartabs.cc/'
URL = 'http://www.guitartabs.cc/search.php?tabtype=any&band={}&song={}'


class IndexView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist_string = self.request.GET.get('artist_string')
        song_string = self.request.GET.get('song_string')
        content = requests.get(URL.format(artist_string, song_string)).content
        soup = BeautifulSoup(content).find(class_='tabslist')
        context['search_results'] = soup.prettify()
        return context


class TabView(TemplateView):
    template_name = 'tab_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = BASE_URL + context.get('url')
        content = requests.get(url).content
        soup = BeautifulSoup(content)
        context['tabs'] = [tab.prettify() for tab in soup.find_all('pre')]
        return context


class ArtistSongsView(TemplateView):
    template_name = 'artist_song_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = BASE_URL + context.get('artist_url')
        content = requests.get(url).content
        soup = BeautifulSoup(content)
        context['songs'] = [song.prettify() for song in soup.find_all(class_='ryzh2')]
        return context


class TopTabsView(TemplateView):
    template_name = 'top_tabs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = BASE_URL + 'top_tabs.html'
        soup = BeautifulSoup(requests.get(url).content)
        context['search_results'] = soup.find(class_='tabslist').prettify()
        return context

