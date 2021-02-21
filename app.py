import requests  # requests 라이브러리 설치 필요
from pymongo import MongoClient
from flask import Flask, render_template

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=950', headers=headers)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', subject="안녕하세요. 반갑습니다.")


if __name__ == "__main__":
    app.run()
