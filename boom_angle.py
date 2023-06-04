import math

item = {"xt": 0.554785, "yt": 0.630466}
player = {"x": 0.705462, "y": 0.318779, "dx": -0.731551, "dy": 0.705462}


pv = (player["dx"], player["dy"])
tv = (item["xt"] - player["x"], item["yt"] - player["y"])

# 计算向量a和向量b的点积
dot_product = pv[0] * tv[0] + pv[1] * tv[1]

# 计算向量a和向量b的模长
norm_a = math.sqrt(pv[0] ** 2 + pv[1] ** 2)
norm_b = math.sqrt(tv[0] ** 2 + tv[1] ** 2)

# 计算向量a和向量b之间的夹角，单位为弧度
angle = math.acos(dot_product / (norm_a * norm_b))

# 将结果转换为度数
angle_degrees = math.degrees(angle)

print(angle_degrees)
