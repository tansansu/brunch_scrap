# 브런치 게시물 스크랩 코드

브런치 글의 글과 사진을 추출하는 함수입니다.

## 사용법
`brunch_to_html()` 함수의 인풋에 브런치 게시물 링크를 넣으면 html문서의 스트링을 리턴합니다.
리턴되는 스트링을 파일로 저장합니다.

### 예
```
url = 'https://brunch.co.kr/@kakao-it/58'

html = brunch_to_html(url)
with(open('folder/test.html', 'w') as f:
    f.write(html)
```
