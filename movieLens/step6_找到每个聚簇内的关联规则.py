# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/6
# file step6_找到每个聚簇内的关联规则.py

import numpy as np
import pandas as pd
import step7_推荐 as s7
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

if __name__ == '__main__':
    # for userId in range(2, 12):
    #     print(userId)
    for userId in range(1,13):
        cluster_num = s7.find_Cluster(userId)
        clusters = s7.creat_user_cluster(cluster_num)
        dic = s7.creat_user_movie_dic(clusters)
        print(len(dic))

        data = []
        for list in dic.values():
            data.append(list)
        # print(data)
        te = TransactionEncoder()
        X = te.fit_transform(data)
        colmns = te.columns_
        df = pd.DataFrame(X, columns=colmns)
        df.astype(np.uint8)
        result = apriori(df, min_support=0.4, use_colnames=True)
        frame = pd.DataFrame(result)
        frame_sort_values = frame.sort_values(by="support", ascending=False)
        tolist = np.array(frame_sort_values).tolist()
        # print(tolist)
        for row in tolist:
            for r in row[1]:
                row[1] = r
        # print(tolist)
        data_frame = pd.DataFrame(tolist)
        print(data_frame)
        data_frame.to_csv("D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\实验数据\\apriori_cluster{}_test.csv".format(userId))



