import json
import requests
import re
import time
import random
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs


def play(video_url):
    #bvid
    bvid = video_url.rsplit("/")[-1]

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    })
    #aid cid
    res = session.get(video_url)
    data_list = re.findall(r'__INITIAL_STATE__=(.+);\(function', res.text)
    data_dict = json.loads(data_list[0])
    aid = data_dict['aid']
    cid = data_dict['videoData']['cid']

    #uuid b_lsid
    js = execjs.compile(open("js.js", mode="r", encoding="utf-8").read())
    _uuid = js.call("u")
    b_lsid = js.call("b")
    session.cookies.set('_uuid', _uuid)
    session.cookies.set('b_lsid', b_lsid)

    session.cookies.set("CURRENT_FNVAL", "4048")
    #buvid4
    res = session.get("https://api.bilibili.com/x/frontend/finger/spi")
    buvid4 = res.json()['data']['b_4']
    session.cookies.set("buvid4", buvid4)
    session.cookies.set("CURRENT_BLACKGAP", "0")
    session.cookies.set("blackside_state", "0")

    res = session.get(
        url='https://api.bilibili.com/x/player/v2',
        params={
            "cid": cid,
            "aid": aid,
            "bvid": bvid,
        }
    )

    ctime = int(time.time())
    res = session.post(
        url="https://api.bilibili.com/x/click-interface/click/web/h5",
        data={
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "part": "1",
            "mid": "0",
            "lv": "0",
            "ftime": ctime - random.randint(100, 500),  # 浏览器首次打开时间
            "stime": ctime,
            "jsonp": "jsonp",
            "type": "3",
            "sub_type": "0",
            "from_spmid": "",
            "auto_continued_play": "0",
            "refer_url": "",
            "bsource": "",
            "spmid": ""
        }
    )

    # print(res.text)

def get_video_id_info(video_url,):
    session = requests.Session()
    bvid = video_url.rsplit('/')[-1]
    res = session.get(
        url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid),

    )
    cid = res.json()['data'][0]['cid']
    res = session.get(
        url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, bvid),
    )
    res_json = res.json()
    aid = res_json['data']['aid']
    view_count = res_json['data']['stat']['view']
    duration = res_json['data']['duration']
    print("\n视频 {}，平台播放量为：{}".format(bvid, view_count))
    session.close()
    return aid, bvid, cid, duration, int(view_count)




def run():
    video_url = "https://www.bilibili.com/video/BV1N94y1R7K5"
    aid, bvid, cid, duration, view_count = get_video_id_info(video_url)
    while True:
        try:
            get_video_id_info(video_url)
            play(video_url)
            view_count += 1
            print("理论刷的播放量：", view_count)
        except Exception as e:
            pass

if __name__ == '__main__':
    run()