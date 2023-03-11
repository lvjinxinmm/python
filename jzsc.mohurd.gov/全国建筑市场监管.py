import random
import time

import requests
from functools import partial
import subprocess
import requests
import json
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
js = execjs.compile(open("js.js", mode="r", encoding="utf-8").read())
#https://jzsc.mohurd.gov.cn/data/company

def AES(url):
    # url = "https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh,zh-CN;q=0.9,zh-TW;q=0.8",
        "Connection": "keep-alive",
        "accessToken": "",
        "Referer": "https://jzsc.mohurd.gov.cn/data/company",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "timeout": "30000"
    }
    cookies = {
        "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1677283646",
        "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1677283646"
    }
    params = {
        "pg": "1",
        "pgsz": "15",
        "total": "450"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    resp = response.text
    dic = js.call("fn", resp)
    list = json.loads(dic)
    list = list['data']['list']
    for child in list:
        id = child['QY_ID']
        child_aes(id)
        # print(id)
        # time.sleep(random.uniform(0.5,1))
def child_aes(id):
    url = "https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/caDetailList"
    params = {
        "qyId": id,
        "pg": "0",
        "pgsz": "15"
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh,zh-CN;q=0.9,zh-TW;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://jzsc.mohurd.gov.cn/data/company/detail?id=002105291239451337",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        # "accessToken": "jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLUcCItjtNJT8gBUMZXLUfLthpUUKvcMtoMqfGfwdLCb8g==",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "timeout": "30000",
        "accessToken": "jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLW6+v0a3bIRfxOk4rs8fPEthpUUKvcMtoMqfGfwdLCb8g=="

    }
    cookies = {
        "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1677283646",
        "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1677303341"
    }
    response = requests.get(url, headers=headers, cookies=cookies,params=params)
    print(response)
    dic = js.call("fn", response.text)
    list = json.loads(dic)
    print(list)


if __name__ == '__main__':
    AES("https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list")