import json

import requests
import subprocess
from functools import partial
import execjs
subprocess.Popen = partial(subprocess.Popen,encoding = "utf-8")
session = requests.session()
session.headers = {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",

}
data = {
    "question": "20221013涨停",
    "source": "ths_mobile_iwencai",
    "user_id": "0",
    "user_name": "0",
    "version": "2.0",
    "secondary_intent": "stock",
    'add_info': '{"urp":{"scene":3,"company":1,"business":1},"contentType":"json"}',
    'log_info': '{"input_type":"click"}',
    'rsh': 'Ths_iwencai_Xuangu_f0oacsmx7ettjf0r6br5f2p3bzogid5w'
}

f = open("11.js",mode='r',encoding="utf-8")
js = execjs.compile(f.read())
v = js.call("fn")
# print(v)
stat_url = 'http://www.iwencai.com/unifiedwap/unified-wap/v2/result/get-robot-data'
resp = session.post(stat_url, data=json.dumps(data, separators=(",", ":")), headers={
                "Content-Type": "application/json"
})
session.cookies['v'] =v
print(resp.text)