import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs



def ll():
    min_behot_time = 1664884732     #不是时间戳
    cookie = {}
    js = execjs.compile(open("js.js", mode="r", encoding="utf-8").read())
    url = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&max_behot_time={}&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web".format(min_behot_time)
    print(url)
    sign = js.call("sign",url)
    url = f"{url}&_signature={sign}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    resp = requests.get(url,headers=headers,cookies=cookie)
    print(resp.text)
    # cookie.update(resp.cookies.get_dict())
    # data_dict = resp.json()
    # print(data_dict['has_more'])
    # for item in data_dict['data']:
    #     print(item['behot_time'], item['title'][0:10])
if __name__ == '__main__':
    ll()
