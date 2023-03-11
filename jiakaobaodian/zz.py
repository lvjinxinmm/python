import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
def ll():
    js = execjs.compile(open("111.js", mode="r", encoding="utf-8").read())
    dic = js.call("fn")
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    url = "https://api2.jiakaobaodian.com/api/open/question/view.htm"
    params = {
        "_r": dic,
        "carType": "car",
        "questionId": "801200",
        "_": "0.13540510901239067"
    }
    response = requests.get(url, headers=headers,  params=params)
    json = response.json()['data']
    print(response.json())
    question = json['question']
    optionA = json['optionA']
    optionB = json['optionB']
    optionC = json['optionC']
    optionD = json['optionD']
    explain = json['explain']
    print(explain)

if __name__ == '__main__':
    ll()