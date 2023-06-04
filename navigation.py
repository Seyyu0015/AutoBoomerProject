import json
import math
import time
import urllib.request

import boom_angle


def navigation():
    found_player = False
    found_base = False

    url = "http://127.0.0.1:8111/map_obj.json"
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    player = {}
    bases = []
    base = {}

    # 找到玩家位置和方向
    for item in data:
        if item["icon"] == "Player":
            found_player = True
            player = {'x': item["x"], 'y': item["y"], "dx": item["dx"], "dy": item["dy"]}
            break

    # 找到战区位置和方向
    for item in data:
        if item["icon"] == "bombing_point":
            found_base = True
            base = {"xt": item["x"], "yt": item["y"]}
            bases.append(base)

    # 判断是否有足够的数据
    if found_base is False or found_player is False:
        return 0

    # 计算战区和玩家的夹角
    else:
        chose_base_ag = None
        i = 1

        for item in bases:
            x, y, dx, dy, xt, yt = player["x"], player["y"], player["dx"], player["dy"], item["xt"], item["yt"]
            # 计算点1到点2的方向向量
            dx2, dy2 = x - xt, y - yt

            # 计算向量叉积，判断点1需要左转还是右转
            cross_product = dx * dy2 - dx2 * dy

            print('- 和第', i, '个战区的夹角是', cross_product)
            i = i + 1
        # if chose_base_ag is None or abs(chose_base_ag) > angle:
        #     print("- 找到角度更小的战区：", chose_base_ag, " → ", angle)
        #     chose_base_ag = angle
    #
    # if chose_base_ag < 0:
    #     print("【】left")
    # else:
    #     print("【】right")


while True:
    print('')
    time.sleep(0.4)
    print(navigation())
