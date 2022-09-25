# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/9/25
# file test.py
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

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

    dic = creat_user_movie_dic()
    data = []
    for list in dic.values():
        data.append(list)
    # print(data)
    result = apriori(transactions=data, min_confidence=0.4, min_support=0.4)
    print(list(result))

if __name__ == '__main__':
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    df
    res = apriori(df, min_support=0.6)
    print(res)