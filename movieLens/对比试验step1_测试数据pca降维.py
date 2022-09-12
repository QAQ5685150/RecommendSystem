# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/7
# file 对比试验step1_测试数据pca降维.py
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

pd.set_option('display.max_columns', None)
data = pd.read_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\user_category.csv",encoding='utf-8',header=None,sep = None)
train_data = np.array(data)
# print(train_data)
all_list=train_data.tolist()#转换list
# print(all_list)

points = []

for item in all_list:
    point = [item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28],
             item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36]]
    points.append(point)

# print(type(points))#每个点存入列表
points = np.array(points)#转化为数组形式
print(points)

pca = PCA(n_components=2)   #降到2维
pca.fit(points)                  #训练
newPoints=pca.fit_transform(points)   #降维后的数据
# PCA(copy=True, n_components=2, whiten=False)
print("前两维的贡献率分别为：", pca.explained_variance_ratio_)  #输出贡献率
print("-----------------------")
print(newPoints)                  #输出降维后的数据
zuobiao = pd.DataFrame(newPoints)
zuobiao.to_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\movieLens_train_zuobiao.csv", index=False,encoding='utf-8')
