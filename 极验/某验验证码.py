import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
f = open("第一个w.js", mode="r", encoding="utf-8")
first_js = execjs.compile(f.read())

f = open("第二个w.js", mode="r", encoding="utf-8")
second_js = execjs.compile(f.read())

f = open("第三个w.js", mode="r", encoding="utf-8")
third_js = execjs.compile(f.read())

import requests
import time
import re
import json
from urllib.parse import urljoin
from util import get_now, jsonp_handle, download_img, trun_back, get_x, get_slide_track

session = requests.session()
session.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

# ============第一次请求, 注册验证码===================

regist_url = f"https://www.geetest.com/demo/gt/register-slide?t={get_now()}"
regist_resp = session.get(regist_url)
regist_dict = regist_resp.json()
gt = regist_dict['gt']
challenge = regist_dict['challenge']

# ============第二次请求. 访问gettype =================
get_type_url = "https://apiv6.geetest.com/gettype.php"
get_type_params = {
    "gt": gt,
    "callback": f"geetest_{get_now()}"
}

get_type_resp = session.get(get_type_url, params=get_type_params)
# print(get_type_resp.text)

# ================第三次请求, 访问第一波get.php ======================
first_get_url = "https://apiv6.geetest.com/get.php"

first_get_dict = first_js.call("cul_first_w", gt, challenge)

# 获取第一次计算之后的aeskey
aeskey = first_get_dict['aeskey']
finger_print = first_get_dict['finger_print']

first_get_params = first_get_dict['msg']
first_get_params['callback'] = f"geetest_{get_now()}"

first_get_resp = session.get(first_get_url, params=first_get_params)
first_get_resp_dict = jsonp_handle(first_get_resp.text)

s = first_get_resp_dict.get("data").get('s')

# 第一次发送请求到https://api.geetest.com/ajax.php

second_w = second_js.call('cul_second_w', aeskey, gt, challenge, s, finger_print)

first_ajax_url = "https://api.geetest.com/ajax.php"
first_ajax_params = {
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "pt": 0,
    "client_type": "web",
    "w": second_w,
    "callback": f"geetest_{get_now()}"
}

first_ajax_resp = session.get(first_ajax_url, params=first_ajax_params)
# print(first_ajax_resp.text)

# 第二次发送get.php
second_get_url = "https://api.geetest.com/get.php"
second_get_params = {
    "is_next": "true",
    "type": "slide3",
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "https": "true",
    "protocol": "https://",
    "offline": "false",
    "product": "popup",
    "api_server": "api.geetest.com",
    "isPC": "true",
    "autoReset": "true",
    "width": "100%",
    "callback": f"geetest_{get_now()}",
}

second_get_resp = session.get(second_get_url, params=second_get_params)
second_get_dict = jsonp_handle(second_get_resp.text)

new_challenge = second_get_dict['challenge']

bg_url = second_get_dict['bg']
fullbg_url = second_get_dict['fullbg']
slice_url = second_get_dict['slice']
s = second_get_dict['s']
c = second_get_dict['c']



# url的拼接, 如果你找不到合适的url进行拼接. 去抓包里找.
static_url = "https://static.geetest.com"
bg_url = urljoin(static_url, bg_url)
fullbg_url = urljoin(static_url, fullbg_url)
slice_url = urljoin(static_url, slice_url)

# print(bg_url)
# print(fullbg_url)
# print(slice_url)

download_img("bg.jpg", bg_url, session)
download_img("fullbg.jpg", fullbg_url, session)
download_img("slice.jpg", slice_url, session)

trun_back("bg.jpg")
trun_back("fullbg.jpg")


"""
var c = [12, 58, 98, 36, 43, 95, 62, 15, 12];
var s = '38423956';

var guiji = [];
var gt = "019924a82c70bb123aae90d483087f94"
var chall = "d59b6ea4c615e1e0b370958ac10a2804ah"
// third_w(gt, challenge, s, c, x_jvli, guiji, tuodongshijian)
console.log(third_w(gt, chall, s, c, 201, guiji, 624))
"""

x_jvli = get_x()
gui, shijian = get_slide_track(x_jvli)
# 计算最后一个w
r = third_js.call("third_w", gt, new_challenge, s, c, x_jvli, gui, shijian)

# 组装callback
r["callback"] = f"geetest_{get_now()}"

second_ajax_url = "https://api.geetest.com/ajax.php"

resp = session.get(second_ajax_url, params=r)

# 滑动验证过了. 怎么用
val_dict = jsonp_handle(resp.text)
validate = val_dict['validate']

# 验证
verify_url = "https://www.geetest.com/demo/gt/validate-slide"
form_data = {
    "geetest_challenge": new_challenge,
    "geetest_validate": validate,
    "geetest_seccode": validate+"|jordan"
}

final_resp = session.post(verify_url, form_data)
print(final_resp.text)
