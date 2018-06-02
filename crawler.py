import os
import requests
from bs4 import BeautifulSoup


def webtoon_name_crawler(webname):
    file_path = 'data/webotoon_list.html'
    webtoon_url = 'https://comic.naver.com/webtoon/weekday.nhn'
    if os.path.exists(file_path):
        html = open(file_path, 'rt').read()
    else:
        response = requests.get(webtoon_url)
        html = response.text
        open(file_path,'wt').write(html)

    soup = BeautifulSoup(html, 'lxml')
    webtoon_title = soup.select('a.title')
    webtoon_name_list = []
    for webtoon_name in webtoon_title:
        webtoon_name_list.append(webtoon_name.get_text(strip=True))
        webtoon_list = set(webtoon_name_list)

    return list(webtoon_list)


if __name__=='__main__':
    while True:
        webtoon_title = input('0: 검색종료 \n'
                              '검색할 웹툰명을 입력해 주세요: ')
        if webtoon_title == '0':
            break
        else:
            webtoon_search = webtoon_name_crawler(webtoon_title)
            i = 0
            for webtoon_search_title in webtoon_search:
                if webtoon_title in webtoon_search_title:
                    i += 1
                    print(f'{i}: {webtoon_search_title}')
        select = input('0: 이전으로 돌아가기\n'
                       '선택: ')
