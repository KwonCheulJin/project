import requests  # requests 라이브러리 설치 필요
from pymongo import MongoClient
from flask import Flask, render_template, jsonify

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.
collect = db.lotto

# # 타겟 URL을 읽어서 HTML를 받아오고,
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=950', headers=headers)
#
# lotto_num = data.json()

# episodes = ['945', '946', '947', '948', '949', '950', '951']
#
#
# def get_request_by_episode(episode):
#     params = {
#         'method': 'getLottoNumber',
#         'drwNo': episode
#     }
#
#     # verify=False SSL 무시
#     req = requests.get('https://www.dhlottery.co.kr/common.do', params=params)
#     result = req.json()
#     return result
#
#
# for episode in episodes:
#     collect.insert_one(get_request_by_episode(episode))
app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lotto', methods=['GET'])
def read_lotto_num():
    lotto_nums = list(collect.find({}, {'_id': 0}))
    print(lotto_nums)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
