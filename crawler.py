from utils import *



def webtoon_name_crawler():
    # 결과값으로 웹툰이름을 키로, id를 값으로 갖는 딕셔너리를 리턴
    # file_path에 해당하는 파일이 있다면 open
    # 없다면 생성후 open
    file_path = 'data/webotoon_list.html'
    webtoon_url = 'https://comic.naver.com/webtoon/weekday.nhn'
    if os.path.exists(file_path):
        html = open(file_path, 'rt').read()
    else:
        response = requests.get(webtoon_url)
        html_res = response.text
        html = open(file_path, 'wt').write(html_res)

    soup = BeautifulSoup(html, 'lxml')
    webtoon_tag = soup.select('a.title')
    p = re.compile(r'/.*titleId=(\d+).*')
    webname_id_dict = dict()
    for title, id in zip(webtoon_tag, webtoon_tag):
        id_search = id.get('href')
        title_id = re.findall(p, id_search)
        webtoon_name = title.get_text()
        webname_id_dict[webtoon_name] = title_id
    return webname_id_dict



if __name__=='__main__':
    while True:
        webtoon_title = input('CTRL + C로 종료합니다 \n'
                              '검색할 웹툰명을 입력해 주세요: ')
        creat_list = webtoon_name_crawler()
        for webname in creat_list:
            if webtoon_title in webname:
                print(f'{webname}')

        select = input('상세보기 할 웹툰: ')
        for title,test_id in creat_list.items():
            if select == title:
                print(f'현재 선택된 웹툰: {title}')
                webtoon = Webtoon(''.join(test_id))
                webtoon.set_info()
                print(f'{webtoon.title}\n'
                      f'  작가: {webtoon.author}\n'
                      f'  설명: {webtoon.description}')











