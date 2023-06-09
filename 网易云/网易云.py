from functools import partial
import subprocess
import requests
import execjs
import json



subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
data = {
    "ids": f"[{input('请输入一个歌曲的id:')}]",  # 输入歌曲的id  "[歌曲id]"
    "level": "standard",
    "encodeType": "aac",
    "csrf_token": ""
}

s = json.dumps(data)

js = execjs.compile(open("评论.js", mode="r", encoding="utf-8").read())
dic = js.call("fn", s)
# print(dic)

real_data = {
    "params": dic['encText'],
    "encSecKey": dic['encSecKey']
}



url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
# url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
resp = requests.post(url, data=real_data, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

print(resp.text)