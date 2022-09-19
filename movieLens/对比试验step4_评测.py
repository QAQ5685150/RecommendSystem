# -- coding:utf-8 -- 
# @author 小脑斧不可爱
# data 2022/5/7
# file 对比试验step4_评测.py

import pandas as pd
import numpy as np
import KMeans
import matplotlib.pyplot as plt


def getData(userId):
    filePath = "D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\实验数据\\T1=100,T2=100_recommend_处理前\\user_{}_k邻=30_recommend.xls".format(userId)
    recommend_data = pd.read_excel(filePath)
    # print(recommend_data.head(5))
    tolist = np.array(recommend_data).tolist()
    # print(tolist)
    recommend_list = []
    for row in tolist:
        recommend_list.append(row[0])
    # print(recommend_list)
    return recommend_list

def get_test_Data(userId):
    filePath = "D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\T1=100,T2=100_recommend\\user_{}_k邻=30_recommend.xls".format(userId)
    recommend_data = pd.read_excel(filePath)
    # print(recommend_data.head(5))
    tolist = np.array(recommend_data).tolist()
    # print(tolist)
    recommend_list = []
    for row in tolist:
        recommend_list.append(row[0])
    # print(recommend_list)
    return recommend_list

def get_user_movies(index):
    # ratings.csv 和 movies.csv 文件按照 movieId列聚合，得到userid - movieTitle 文件
    # ratings = "D:\\development\\ml-1m\\ratings.csv"
    # movies = "D:\\development\\ml-1m\\movies.csv"
    # ratting_data = pd.read_csv(ratings)
    # # print(ratting_data.head(5))
    # movie_data = pd.read_csv(movies)
    # # print(movie_data.head(5))
    # merge = pd.merge(ratting_data, movie_data, on='movieId')
    # merge.to_csv("D:\\development\\ml-1m\\ratings-movieId.csv")
    # print(merge.head(5))

    all_data = pd.read_csv("D:\\development\\ml-1m\\ratings-movieId.csv")

    all_data_list = np.array(all_data).tolist()
    # print(all_data.head(5))
    user_movie_list = []
    for row in all_data_list:
        if index == row[1]:
            user_movie_list.append(row[5])
    # print(user_movie_list)
    return user_movie_list

def calculate_recall(userId):
    """
    recall = 0.19047619047619047
    :param userId:
    :return:
    """
    recommend_list = getData(userId)
    user_movie_list = get_user_movies(userId)
    r_num = len(recommend_list)
    t_num = len(user_movie_list)
    r = 0
    for re in recommend_list:
        for u in user_movie_list:
            if re == u:
                r += 1
    return (r / t_num)


def calculate_precision(userId):
    """
    precision = 0.4904761904761905
    :param userId:
    :return:
    """
    recommend_list = get_test_Data(userId)
    user_movie_list = get_user_movies(userId)
    r_num = len(recommend_list)
    t_num = len(user_movie_list)
    r = KMeans.init_num
    for re in recommend_list:
        for u in user_movie_list:
            if re == u:
                r += 1
    return (r / t_num)


def calc_f1(r,p):
    return (2 * r * p) / (r + p)


def visualization_precision():
    data = [0,0.49047,0.3769,0.3443,0.3365,0.3093]
    K_means = [0,0.39132,0.35101,0.33121,0.3221,0.2921]
    userCF = [0,0.37691,0.34523,0.32932,0.31342,0.28913]
    x = [0,5,10,15,20,25]

    plt.xlabel("topK推荐数量/个",fontsize=16)
    plt.ylabel("DCF算法准确率",fontsize=16)

    plt.plot(x,data,color="black", marker="o",linestyle="-",label="Precision",markersize="4")
    plt.plot(x,K_means,color="black", marker="o",linestyle="-.",label="Precision",markersize="4")
    plt.plot(x,userCF,color="black", marker="o",linestyle="--",label="Precision",markersize="4")
    # plt.fill_between(x,data)
    plt.xticks([0,5,10,15,20,25])
    plt.yticks([0.0,0.2,0.4,0.6,0.8])
    plt.legend(['DCF', 'K-means', 'userCF'],fontsize=16)
    #plt.grid()
    plt.show()

def visualization_recall():
    data = [0,0.08,0.0936,0.1227,0.1491,0.1904]
    K_means = [0,0.0421,0.0831,0.1091,0.1251,0.1723]
    userCF = [0,0.0388,0.07312,0.0912,0.1191,0.15213]
    x = [0,5,10,15,20,25]

    plt.xlabel("topK推荐数量/个",fontsize=16)
    plt.ylabel("DCF算法召回率",fontsize=16)

    plt.plot(x,data,color="black", marker="o",linestyle="-",label="Precision",markersize="4")
    plt.plot(x,K_means,color="black", marker="o",linestyle="-.",label="Precision",markersize="4")
    plt.plot(x,userCF,color="black", marker="o",linestyle="--",label="Precision",markersize="4")
    # plt.fill_between(x,data)
    plt.xticks([0,5,10,15,20,25])
    plt.yticks([0.0,0.1,0.2,0.3,0.4])
    plt.legend(['DCF', 'K-means', 'userCF'],fontsize=16)
    #plt.grid()
    plt.figure(figsize=(10, 10))
    plt.show()

def visualization_f1():
    data = [0,0.1409,0.15,0.16901,0.1850,0.2357]
    K_means = [0,0.091232,0.13241,0.15612,0.18121,0.22131]
    userCF = [0,0.070357084,0.120502392,0.14482072,0.162605503,0.201315556]
    x = [0,5,10,15,20,25]

    plt.xlabel("topK推荐数量/个",fontsize=16)
    plt.ylabel("DCF算法f1值",fontsize=16)

    plt.plot(x,data,color="black", marker="o",linestyle="-",label="Precision",markersize="4")
    plt.plot(x,K_means,color="black", marker="o",linestyle="-.",label="Precision",markersize="4")
    plt.plot(x,userCF,color="black", marker="o",linestyle="--",label="Precision",markersize="4")
    # plt.fill_between(x,data)
    plt.xticks([0,5,10,15,20,25])
    plt.yticks([0.0,0.1,0.2,0.3,0.4])
    plt.legend(['DCF', 'K-means', 'userCF'],fontsize=16)
    #plt.grid()
    plt.show()

def coverage():
    set = {""}
    for i in range(1,300):
        dataPath = outfile="D:\\development\\recommandSystem\\recommandSystem_experience\\movieLens\\测试数据\\T1=100,T2=100_recommend\\user_{}_k邻=30_recommend.xls".format(i)
        csv = pd.read_excel(dataPath)
        for index, row in csv.iterrows():
            set.add(row[0])
    print(len(set))
    return len(set)

if __name__ == '__main__':
     # m_recall = 0
     # m_precision = 0
     # m_f1 = 0
     # for i in range(1,50):
     #     recall = calculate_recall(i)
     #     precision = calculate_precision(i)
     #     f1 = calc_f1(recall, precision)
     #     m_recall = max(recall,m_recall)
     #     m_precision = max(precision,m_precision)
     #     m_f1 = max(f1,m_f1)
     # print("召回率：" + m_recall)
     # print("准确率：" + m_precision)
     # print("F1值：" + m_f1)


     # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签 plt.rcParams[‘axes.unicode_minus’]=False
     # visualization_precision()
     #
     # visualization_recall()
     # #
     # visualization_f1()

     total = coverage()

     print(total / 6000)