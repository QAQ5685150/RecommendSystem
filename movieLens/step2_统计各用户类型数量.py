# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/5
# file step2_统计各用户类型数量.py

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# data = pd.read_csv("D:\\development\\py_project\\hello_world\\movieLens\\实验数据\\实验数据_test_clear.csv")
data = pd.read_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\测试数据_test_clear.csv")
print(data.head(5))
name_dic = {"Action": 0, "Adventure": 1, "Animation": 2, "Children": 3, "Comedy": 4,
            "Crime": 5, "Documentary": 6, "Drama": 7, "Fantasy": 8, "Film-Noir": 9,
            "Horror": 10, "Musical": 11, "Mystery": 12, "Romance": 13, "Sci-Fi": 14,
            "Thriller": 15, "War": 16, "Western": 17}

user_movie_list = np.zeros((671, 18))

print(user_movie_list)

i = 0
j = 0
for index, row in data.iterrows():
    split = row[2].split("|")
    if row[3] == i + 1 :
        for s in split :
            user_movie_list[i][name_dic.get(s,0)] += 1
    else:
        i += 1
        if row[3] == i + 1:
            for s in split:
                user_movie_list[i][name_dic.get(s, 0)] += 1

print(user_movie_list)
lieming=["Action", "Adventure", "Animation", "Children", "Comedy",
            "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir",
            "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
            "Thriller", "War", "Western"]
user_category = pd.DataFrame(columns=lieming,data=user_movie_list)
# user_category.to_csv("D:\\development\\py_project\\hello_world\\movieLens\\实验数据\\user_category.csv", index=False,encoding='utf-8')
user_category.to_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\user_category.csv", index=False,encoding='utf-8')