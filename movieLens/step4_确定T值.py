# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/5
# file step4_确定T值.py
import math
import numpy as np
import pandas as pd


def distance(point1,point2):
    return math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2))

points = []
center_points = []
K = 0
file="D:\\development\\py_project\\hello_world\\movieLens\\实验数据\\movieLens_train_zuobiao2.csv"
data=pd.read_csv(file)
train_data = np.array(data)#np.ndarray()每个姓名转换为一个list[]
#print(type(train_data))
all_list=train_data.tolist()#转换list
#print(all_list)

for item in all_list:
    print(item[1])
    print(item[2])
    print("-----------------------")
    point = [item[1], item[2]]
    points.append(point)

#print(type(points))#每个点存入列表
points = np.array(points)#转化为数组形式
#print(points)

T = 0
for item in points:
    avg = 0
    for other in points:
        if all(other == item):
            continue
        avg += distance(item,other)
    avg /= 671
    print("当前点的平均距离为：",avg)
    T += avg
T /= 672
print("T值为：",T)