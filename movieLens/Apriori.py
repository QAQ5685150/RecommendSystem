# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/6
# file Apriori.py
import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

ratings_path = "D:\\development\\data_set\\ml-1m\\ratings.dat"
movie_path = "D:\\development\\data_set\\ml-1m\\movies.dat"

def creat_user_movie_dic():
    dic={}
    file = "D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\apriori\\all_data.csv"
    data = pd.read_csv(file,encoding='utf-8')
    all_data = np.array(data)  # np.ndarray()每个姓名转换为一个list[]
    all_list = all_data.tolist()  # 转换list
    print(len(all_list))
    # print(all_list)
    for item in all_list:
        # print(item[0])
        dic.setdefault(item[3], []).append(item[1])#将电影名加入对应用户的字典内，键为用户名，值为电影列表
    return dic

def getData():
    # ratings_csv = pd.read_csv(ratings_path)
    # movies_csv = pd.read_csv(movie_path)

    train = []
    test = []

    dic = creat_user_movie_dic()
    data = []
    for list in dic.values():
        data.append(list)
    # print(data)
    te = TransactionEncoder()
    X = te.fit_transform(data)
    colmns = te.columns_
    df = pd.DataFrame(X, columns=colmns)
    print(df)
    df.astype(np.uint8)
    result = apriori(df, min_support=0.3, use_colnames=True)
    print(result)
    frame = pd.DataFrame(result)
    frame_sort_values = frame.sort_values(by="support", ascending=False)
    tolist = np.array(frame_sort_values).tolist()
    # print(tolist)
    # for row in tolist:
    #     for r in row[1]:
    #         row[1] = r
    # print(tolist)
    data_frame = pd.DataFrame(tolist)
    data_frame.to_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\apriori\\apriori_rule.csv")
    print(data_frame)

if __name__ == '__main__':
    getData()
