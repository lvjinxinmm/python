import time
import json
import datetime
import random
import binascii
import ctypes
from urllib.parse import urlencode, urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor

import execjs
import requests
from Crypto.Cipher import AES

body = """
function fn(){
    var t = (new Date).getTime().toString(36)
      , r = Math.random().toString(36).replace(/^0./, "");
    return e = "".concat(t, "_").concat(r)
}
function qn(){
    var Le = -5516;
    var Yn = 0
    var Vn = '"|g0000648jiz|1678409572|mg3c3b04ba|1.25.0|lf1ri881_3548pmhudyv|4330701|https://w.yangshipin.cn/|mozilla/5.0 (windows nt ||Mozilla|Netscape|Win32|"'
    for (Ur = 0; Ur < Vn["length"]; Ur++){
        Xn = Vn["charCodeAt"](Ur),
        Yn = (Yn << Le + 1360 + 9081 - 4920) - Yn + Xn,
        Yn &= Yn;
    }
    qn = Yn;
    return qn;
}
"""
js = execjs.compile(body)
guid = js.call("fn")
pid = js.call("fn")

js = execjs.compile(body)
qn = js.call("qn")

def aes_encrypt(text):
    """
    AES加密
    """
    # "4E2918885FD98109869D14E0231A0BF4"
    # "16B17E519DDD0CE5B79D7A63A4DD801C"

    key = binascii.a2b_hex('4E2918885FD98109869D14E0231A0BF4')
    iv = binascii.a2b_hex('16B17E519DDD0CE5B79D7A63A4DD801C')
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text = text.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypt_bytes = cipher.encrypt(text)
    return binascii.b2a_hex(encrypt_bytes).decode()


def create_ckey(vid, ctime, app_ver, platform, guid):
    ending = "https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"
    data_list = ["", vid, ctime, "mg3c3b04ba", app_ver, guid, platform, ending]
    data_string = "|".join(data_list)
    qn = js.call('qn', data_string)
    encrypt_string = "|{}{}".format(qn, data_string)
    ckey = "--01" + aes_encrypt(encrypt_string).upper()

    return ckey


def get_video_info(vid, ctime, app_ver, platform, flow_id, guid, ckey):
    params = {
        "callback": "jsonp1",
        "guid": guid,
        "platform": platform,
        "vid": vid,
        "defn": "hd",
        "charge": "0",
        "defaultfmt": "auto",
        "otype": "json",
        "defnpayver": "1",
        "appVer": app_ver,
        "sphttps": "1",
        "sphls": "1",
        "spwm": "4",
        "dtype": "3",
        "defsrc": "2",
        "encryptVer": "8.1",
        "sdtfrom": platform,
        "cKey": ckey,
        "panoramic": "false",
        "flowid": flow_id
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'referer': 'https://m.yangshipin.cn/',
    }

    res = requests.get(
        url="https://playvv.yangshipin.cn/playvinfo",
        params=params,
        headers=headers,
        cookies={
            "guid": guid
        }
    )
    res.close()

    text = res.text.strip("jsonp1")[1:-1]
    info_dict = json.loads(text)
    return info_dict


def play(platform, guid, video_url, vid, pid, vurl):
    data = {
        "ctime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ua": "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/102.0.0.0 safari/537.36",
        "hh_ua": "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/102.0.0.0 safari/537.36",
        "platform": platform,
        "guid": guid,
        "Pwd": "1698957057",
        "version": "wc-1.2.6",
        "url": video_url,
        "hh_ref": video_url,
        "vid": vid,
        "isfocustab": "1",
        "isvisible": "1",
        "idx": "0",
        "val": "428",
        "pid": pid,
        "bi": "0",
        "bt": "0",
        "defn": "hd",
        "vurl": vurl,
        "step": "6",
        "val1": "1",
        "val2": "1",
        "fact1": "",
        "fact2": "",
        "fact3": "",
        "fact4": "",
        "fact5": ""
    }
    res = requests.post(
        url="https://btrace.yangshipin.cn/kvcollect",
        params={"BossId": "2865"},
        data=data,
        headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'referer': 'https://m.yangshipin.cn/',
        }
    )


def task(video_url):
    try:
        # https://w.yangshipin.cn/video?type=0&vid=g0000648jiz
        vid = parse_qs(urlparse(video_url).query)['vid'][0]

        guid = js.call('fn')
        pid = js.call('fn')

        flow_id = pid
        platform = "4330701"
        app_ver = "1.22.0"
        ctime = str(int(time.time()))

        ckey = create_ckey(vid, ctime, app_ver, platform, guid)

        video_info_dict = get_video_info(vid, ctime, app_ver, platform, flow_id, guid, ckey)
        vkey = video_info_dict["vl"]['vi'][0]['fvkey']
        fn = video_info_dict["vl"]['vi'][0]['fn']

        vurl = f"https://mp4playcloud-cdn.ysp.cctv.cn/{fn}?sdtfrom={platform}&guid={guid}&vkey={vkey}&platform=2"

        play(platform, guid, video_url, vid, pid, vurl)
    except Exception as e:
        print(e)


def run():
    video_url = "https://w.yangshipin.cn/video?type=0&vid=n000046gh5d"  # 1905  2205

    start = time.time()

    pool = ThreadPoolExecutor(30)
    for i in range(10):
        pool.submit(task, video_url)
    pool.shutdown()

    end = time.time()

    print("执行完成，耗时：", end - start)


if __name__ == '__main__':
    run()