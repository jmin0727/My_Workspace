from flask import Flask, render_template  # Flask = 클래스
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)   #클래스 생성자 띄워놈

@app.route("/")     #주소 이름
def hello_world():
    a = add(4, 3)
    print(a)

    b = ytn_craw()      #크롤링값

    c = { "x": ["Mar 1", "Mar 2", "Mar 3"], "y": [10000, 30162, 26263] }      #차트에 있는 데이터들을 c에 넣기 위해 딕셔너리로 가져온거

    d = {"x": ["January", "February", "March", "April"], "y": [4215, 5312, 6251, 7841] }

    return render_template("index.html", MY_ADD=a, MY_YTN_LIST=b, MY_CHART_DICT=c, MY_BAR_CHART_DICT=d)          #html 템플릿을 불러들이다 = 렌더링하다


def ytn_craw() :
    mylist = []    #리턴 변수 선언

    url = "https://star.ytn.co.kr/news/list.php?mcd=0117&hcd=04"
    res = requests.get(url)
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    news_list = soup.select("#container > div > div.content > div > div.news_list_wrap > div")
    for news in news_list:
        title = news.select_one("div.text_area > div.title > a").text
        rdate = news.select_one("div.text_area > div.info > div.date").text
        img = news.select_one("div.photo > a > img").get("data-src")
        href = news.select_one("div.text_area > div.title > a").get("href")
        #print(title, rdate, img, href)
        mylist.append( { "title":title, "rdate":rdate, "img":img, "href":href } )

    #{'title': '아이들 소연, 5년 2개월 만에 솔로 컴백…9월 초 출격', 'rdate': '2026.08.19. 13:09',
    #'img': 'https://image.ytn.co.kr/general/jpg/2026/0819/202608191309270831_h.jpg',
    #'href': 'https://star.ytn.co.kr/_sn/0117_202608191309270831'},
    # {'title': '로이킴, 임영웅·이찬원·추영우 이어 김종국까지…작사·작곡가로 영역 확장', 'rdate': '2026.08.19. 11:12',
    #'img': 'https://image.ytn.co.kr/general/jpg/2026/0819/202608191112438733_h.jpg', 'href': 'https://star.ytn.co.kr/_sn/0117_202608191112438733'}


    return mylist



def add(num1, num2):
    res = num1 + num2
    return res


#port : 실행중인 프로세스/프로그램의 고유 번호  (http 기본 port = 80, https = 443)

if __name__ == '__main__':    # 여기 이 파일에서 직접 실행하는거라면
    app.run(host='127.0.0.1', port=2727, debug=True)    # run = 구동해라