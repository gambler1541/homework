import re
from bs4 import BeautifulSoup
import requests
import os


class Webtoon:
    def __init__(self,title_id):
        self.title_id = title_id
        self._title = None
        self._author = None
        self._description = None
        self._episode_list = list()
        self._html = ''

    @property
    def html(self):
        if not self._html:
            file_path = 'data/episode_list-{}.html'.format(self.title_id)
            url_episode_list = 'https://comic.naver.com/webtoon/list.nhn'
            params = {
                'titleId': self.title_id
            }

            if os.path.exists(file_path):
                html = open(file_path, 'rt').read()

            else:

                response = requests.get(url_episode_list, params)
                html = response.text
                open(file_path, 'wt').write(html)

            self._html = html
        return self._html

    def _get_info(self, attr_name):
        if not getattr(self, attr_name):
            self.set_info()
        return getattr(self, attr_name)


    @property
    def title(self):
        return self._get_info('_title')

    @property
    def author(self):
        return self._get_info('_author')

    @property
    def description(self):
        return self._get_info('_description')



    def set_info(self):
        soup = BeautifulSoup(self.html, 'lxml')
        h2_title = soup.select_one('div.detail > h2')
        title = h2_title.contents[0].strip()
        author = h2_title.contents[1].get_text(strip=True)
        description = soup.select_one('div.detail > p').get_text(strip=True)

        self._title = title
        self._author = author
        self._description = description








class Episode:
    pass



class EpisodeImage:
    pass




