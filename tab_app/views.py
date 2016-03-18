from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://www.guitartabs.cc/'
URL = 'http://www.guitartabs.cc/search.php?tabtype=any&band={}&song={}'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist_string = self.request.GET.get('artist_string')
        song_string = self.request.GET.get('song_string')
        content = requests.get(URL.format(artist_string, song_string)).content
        soup = BeautifulSoup(content).find(class_='tabslist')
        for link in soup.find_all('a'):
            link['href'] = reverse('tab_detail_view', kwargs={'url': link['href']})
        context['search_results'] = soup.prettify()
        return context


class TabView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = BASE_URL + context.get('url')
        content = requests.get(url).content
        soup = BeautifulSoup(content)
        context['tabs'] = [tab.prettify() for tab in soup.find_all('pre')]
        return context


