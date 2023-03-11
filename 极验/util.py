"""
e['heiht] = r, 160
e['width'] = 260;
Ut = [x,x,x,xx,x,]
for (var a = r / 2, _ = 0; _ < 52; _ += 1) {
    var c = Ut[_] % 26 * 12 + 1
      , u = 25 < Ut[_] ? a : 0
                            x, y, w, h
      , l = o[getImageData](c, u, 10, a);  // 获取一部分图片
    s[putImageData](l, _ % 26 * 10, 25 < _ ? a : 0); // 把一部分图片画到画布上
}
"""
import time
import re
import json

import cv2


def trun_back(path):
    # python画图的包pillow,  pip install pillow
    from PIL import Image  # Image 就是python的canvas
    old_img = Image.open(path)
    # 创建一张新图
    new_img = Image.new("RGB", (260, 160))
    Ut = [
    39,
    38,
    48,
    49,
    41,
    40,
    46,
    47,
    35,
    34,
    50,
    51,
    33,
    32,
    28,
    29,
    27,
    26,
    36,
    37,
    31,
    30,
    44,
    45,
    43,
    42,
    12,
    13,
    23,
    22,
    14,
    15,
    21,
    20,
    8,
    9,
    25,
    24,
    6,
    7,
    3,
    2,
    0,
    1,
    11,
    10,
    4,
    5,
    19,
    18,
    16,
    17
]
    r = 160
    a = r // 2  # 整数

    for _ in range(52):
        c = Ut[_] % 26 * 12 + 1
        if 25 < Ut[_]:
            u = a
        else:
            u = 0

        # 获取一个区域, (x1, y1, x2, y2)
        l = old_img.crop((c, u, c + 10, u + a))

        x1 = _ % 26 * 10
        if 25 < _:
            y1 = a
        else:
            y1 = 0
        new_img.paste(l, (x1, y1))

    new_img.save(f"new_{path}")


def get_now():
    return int(time.time() * 1000)


def jsonp_handle(text):
    jsonp_re = re.compile(r"\((?P<code>.*)\)", re.S)
    jsonp_str = jsonp_re.search(text, re.S).group("code")
    return json.loads(jsonp_str)


def download_img(name, url, session):
    resp = session.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


# 计算滑块滑动的距离
def get_x():
    # opencv来完成计算
    """
    # 挨个跑...
    pip install python-opencv
    pip install opencv-python
    # x_jvli, guiji, tuodongshijian
    import cv2  # 导入cv2之后没有代码提示. 怎么办?
    :return:
    """
    # 读取两张图
    bg = cv2.imread("new_bg.jpg")
    slice = cv2.imread("slice.jpg")

    # 做灰度处理
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    slice = cv2.cvtColor(slice, cv2.COLOR_BGR2GRAY)

    # 图片边缘处理
    bg_can = cv2.Canny(bg, 255, 255)
    slice = cv2.Canny(slice, 255, 255)

    # 匹配图像的相似度, TM_CCOEFF_NORMED参数固定即可
    r = cv2.matchTemplate(bg_can, slice, cv2.TM_CCOEFF_NORMED)

    # 获取匹配度最好的一个结果
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(r)

    x = maxLoc[0]
    y = maxLoc[1]
    # 为了测试的
    # bg = cv2.rectangle(bg, (x, y), (x+50, y + 50), (255, 255, 255))
    # cv2.imshow("tu", bg)  # 弹窗
    # cv2.waitKey(0)  # 防止程序一闪就没了
    # cv2.destroyAllWindows()  # 关掉所有窗口
    return x


# 三代的极验轨迹..
def __ease_out_expo(sep):
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)


def get_slide_track(distance):
    import random
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append([distance, 0, t])

    return slide_track, t

'''
以下是极验四代的轨迹生成算法
def __ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


def __ease_out_quart(x):
    return 1 - pow(1 - x, 4)


def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """
    ttt = 0
    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(20, 60), random.randint(10, 40), 0]
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t = random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x - _x, _y, t])
        _x = x
        ttt += t
    slide_track.append([0, 0, random.randint(200, 300)])
    return slide_track, ttt


'''
