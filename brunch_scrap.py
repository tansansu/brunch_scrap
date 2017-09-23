'''
브런치 글의 내용을 html파일로 저장해주는 함수
'''

# 2017.09.23

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys

def brunch_to_html(url):
    # 웹페이지 수집
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    articles = soup.findAll(re.compile(r'(p|div|h2|blockquote)'), \
    {'class':re.compile(r'(wrap_item item_type_text|wrap_img_float)')})

    ## 제목 추출
    title = soup.find('h1', {'class':'cover_title'}).text
    ## 소제목 추출
    sub_title = soup.find('p', {'class':'cover_sub_title'}).text
    # 결과물의 body 생성
    body = '<h1>' + title + '</h1><br><h3>' + sub_title + '</h3><br>'
    # 본문에서 텍스트와 그림 링크를 추출하여 body 생성
    for line in articles:
        if str(line).__contains__('div'):
            img_link = re.search(r'http.*', line.find('img')['src']).group(0)
            body += '<img src="' + img_link + '"><br>'
        elif str(line).__contains__('h2'):
            body += '<h2>' + line.text + '</h2><br>'
        elif str(line).__contains__('blockquote'):
            body += '<br><font color="grey">' + line.text + '</font><br>'
        else:
            body += line.text + '<br>'

    # 전체 html 파일 생성
    pad_front = '<html><head></head><body>'
    pad_rear = '</body></html>'
    html = pad_front + body + pad_rear

    return(html)

docs = brunch_to_html(sys.argv[1])

with open('/Volumes/RAMDisk/brunch.html', 'w') as f:
    f.write(docs)