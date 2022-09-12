# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/5
# file step1_切分数据集.py
import pandas as pd
import numpy as np

pd.set_option('display.max_columns',None)

ratings_path = "D:\\development\\ml-1m\\ratings.csv"
movie_path = "D:\\development\\ml-1m\\movies.csv"

ratings_csv = pd.read_csv(ratings_path)
movies_csv = pd.read_csv(movie_path)

train = []
test = []

merge = pd.merge(movies_csv,ratings_csv,  on='movieId')
merge.sort_values
merge.drop('timestamp',1,inplace = True)
merge.sort_values(by="userId" , inplace=True, ascending=True)


for index, row in merge.iterrows():
    #print(index)
    if (index+1)% 5:
        train.append(row)
    else:
        test.append(row)

train_frame = pd.DataFrame(train)
test_frame = pd.DataFrame(test)

train_frame.to_csv("D:\\development\\py_project\\hello_world\\movieLens\\实验数据\\实验数据_test_clear.csv",index=False,encoding='utf-8')
test_frame.to_csv("D:\\development\\py_project\\hello_world\\movieLens\\测试数据\\测试数据_test_clear.csv",index=False,encoding='utf-8')
