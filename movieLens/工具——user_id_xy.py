# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/7
# file 工具——user_id_xy.py
# import pandas as pd
# import numpy as np
#
# file1 = pd.read_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\movieLens_train_zuobiao.csv")
# file2 = pd.read_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\对比实验_user_Cluster_T1=100,T2=100.csv")
#
# tolist1 = np.array(file1).tolist()
# tolist2 = np.array(file2).tolist()
#
# list = [[]]
# index = 0
# for row1 in tolist1:
#     # print(row1)
#     for row2 in tolist2:
#         if row1[2] == row2[0] and row1[3] == row2[1]:
#             list.append(row1)
#
# print(list)

# frame = pd.DataFrame(list)
# frame.to_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\user_id_xy.csv")
