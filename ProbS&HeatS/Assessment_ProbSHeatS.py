#coding=UTF-8
'''
Created on 2016��10��25��

@author: ZWT
'''
import csv
import numpy as np
import random

method = raw_input("请输入1选择ProbS推荐，输入2选择HeatS推荐:")
Re_length = int(raw_input("请输入所需推荐列表的长度:"))
timeNum = int(raw_input("清输入AUC循环次数:"))

TrainSet_CsvFile = u"data/votes.csv"
ScoialSet_CsvFIle = u'data/social.csv'
ProbeSet_CsvFile = u"data/probeSet.csv"

TrainSet_userList = []#训练集user列表
TrainSet_itemList = []#训练集item列表
ProbeSet_userList = []#测试集user列表
ProbeSet_itemList = []#测试集item列表


######训练集TrainSet_CsvFile文件转邻接矩阵
TrainSet = csv.reader(file(TrainSet_CsvFile,'rb'))
TrainSetData = []
for line in TrainSet:
    TrainSet_userList.append(int(line[1])-1)
    TrainSet_itemList.append(int(line[2])-1)
    TrainSetData.append([int(line[1]),int(line[2])])
TrainSet_userList = set(TrainSet_userList)
TrainSet_itemList = set(TrainSet_itemList)
Matrix_Adjacency = np.zeros([len(TrainSet_userList),len(TrainSet_itemList)])
for n in range(len(TrainSetData)):
    i = int(TrainSetData[n][0]) - 1
    j = int(TrainSetData[n][1]) - 1
    Matrix_Adjacency[i,j] = 1
print "邻接矩阵转换："+str(Matrix_Adjacency.shape)

######社交网络ScoialSet_CsvFile文件求社交网络矩阵
ScoialSet = csv.reader(file(ScoialSet_CsvFIle,'rb'))
ScoialSetData = []
ScoialSet_rowList = []
ScoialSet_colList = []
for line in ScoialSet:
    ScoialSet_rowList.append(int(line[0]))
    ScoialSet_colList.append(int(line[1]))
    ScoialSetData.append([int(line[0]),int(line[1])])
ScoialSet_rowList = set(ScoialSet_rowList)
ScoialSet_colList = set(ScoialSet_colList)
Matrix_Scoial = np.zeros([len(ScoialSet_rowList),len(ScoialSet_colList)])
for n in range(len(ScoialSetData)):
    i = int(ScoialSetData[n][0]) - 1
    j = int(ScoialSetData[n][1]) - 1
    Matrix_Scoial[i,j] = 1
print "社交矩阵转换："+str(Matrix_Scoial.shape)

######测试集ProbeSet_CsvFile文件求用户喜欢列表
ProbeSet = csv.reader(file(ProbeSet_CsvFile,'rb'))
ProbeSetData = []
for line in ProbeSet:
    ProbeSet_userList.append(int(line[1])-1)
    ProbeSet_itemList.append(int(line[2])-1)
    ProbeSetData.append([int(line[1]),int(line[2])])
ProbeSet_userList = set(ProbeSet_userList)
ProbeSet_itemList = set(ProbeSet_itemList)

######邻接矩阵求转置矩阵
Matrix_Transposed = Matrix_Adjacency.T
print "转置矩阵转换："+str(Matrix_Transposed.shape)
    
######邻接矩阵和转置矩阵求user的度和item的度，转为对角矩阵再求逆矩阵
degree_user = [sum(Matrix_Adjacency[i]) for i in range(len(Matrix_Adjacency))]
degree_item = [sum(Matrix_Transposed[i]) for i in range(len(Matrix_Transposed))]
degree_scoial = [sum(Matrix_Scoial[i]) for i in range(len(Matrix_Scoial))]

diag_user = np.diag(degree_user)
print "user的度的对角矩阵计算："+str(diag_user.shape)
inv_diag_user = np.linalg.inv(diag_user)
print "user的度的对角矩阵求逆矩阵："+str(inv_diag_user.shape)
diag_item = np.diag(degree_item)
print "item的度的对角矩阵计算："+str(diag_item.shape)
inv_diag_item = np.linalg.inv(diag_item)
print "item的度的对角矩阵求逆矩阵："+str(inv_diag_item.shape)
diag_scoial = np.diag(degree_scoial)
print "scoial的度的对角矩阵计算："+str(diag_item.shape)
inv_diag_scoial = np.linalg.inv(diag_scoial)
print "scoial的度的对角矩阵求逆矩阵："+str(inv_diag_item.shape)

######邻接矩阵，转置矩阵，逆矩阵求物质网络矩阵
if method == "1":
    ProbS_UserItem = np.dot(np.dot(np.dot(Matrix_Transposed,inv_diag_user),Matrix_Adjacency),inv_diag_item)
    print "物质UserItem矩阵计算："+str(ProbS_UserItem.shape)
    ProbS_Scoial = np.dot(np.dot(np.dot(np.dot(np.dot(Matrix_Transposed,inv_diag_user),Matrix_Scoial),inv_diag_scoial),Matrix_Adjacency),inv_diag_item)
    print "物质Scoial矩阵计算："+str(ProbS_Scoial.shape)
    Matrix_Network_UserItem = ProbS_UserItem
    Matrix_Network_Scoial = ProbS_Scoial
elif method == "2":
    HeatS_UserItem = np.dot(np.dot(np.dot(inv_diag_item,Matrix_Transposed),inv_diag_user),Matrix_Adjacency)
    print "热能UserItem矩阵计算："+str(HeatS_UserItem.shape)
    HeatS_Scoial = np.dot(np.dot(np.dot(np.dot(np.dot(inv_diag_item,Matrix_Transposed),Matrix_Scoial),inv_diag_scoial),inv_diag_user),Matrix_Adjacency)
    print "热能Scoial矩阵计算："+str(HeatS_Scoial.shape)
    Matrix_Network_UserItem = HeatS_UserItem
    Matrix_Network_Scoial = HeatS_Scoial
else:
    print "推荐算法选择错误！输入1选择ProbS，输入2选择HeatS"

######计算质量分配
QualityList = []

Params = 1.0
count = 1
while count < 11:
    print "\n"+'这是第 '+str(count)+" 次计算，参数为："+str(Params)
    Precision_List = []
    Recall_List = []
    RSgrade_List = []
    AUCgrade_List =[]

    for user in range(len(TrainSet_userList)):
        #print "USER_ID为 "+str(user)+" 推荐："
        ####user的推荐列表
        userQualityList = []
        Matrix_user_F = Matrix_Adjacency[user]
        Matrix_Wuzhi_UserItem = Params * (np.dot(Matrix_Network_UserItem,Matrix_user_F))
        Matrix_Wuzhi_Scoial = (1-Params) * (np.dot(Matrix_Network_Scoial,Matrix_user_F))
        Matrix_Wuzhi = Matrix_Wuzhi_UserItem + Matrix_Wuzhi_Scoial
        
        for item in range(len(Matrix_Adjacency[user])):
            if (Matrix_Adjacency[user,item] == 0):
                userQualityList.append([item,Matrix_Wuzhi[item],0])
            else:
                userQualityList.append([item,Matrix_Wuzhi[item],1])
        userQualityList = sorted(userQualityList,key = lambda userQualityList:userQualityList[1],reverse=True)
        #按物质量从大到小排序
        userRecommendList = []
        userRsRecommendList  = []

        for item in userQualityList:
            if item[2] == 0:
                userRecommendList.append(item)
                userRsRecommendList.append(item)
        if userRecommendList[Re_length-1][1]==userRecommendList[Re_length][1]:
            tempList = [index for index,x in enumerate(userRecommendList) if x[1]==userRecommendList[Re_length-1][1]]
            randomList = random.sample(tempList,(Re_length - tempList[0]))#randomList存储随机的物质相同的item下标
            userRecommendList = userRecommendList[0:tempList[0]] + [userRecommendList[i]for i in randomList]#截取前段物质不同的列表，加上随机划分的物质相同的列表
        else:
            userRecommendList = userRecommendList[0:(Re_length)]
#         print "USER_ID为"+str(user)+"的推荐列表如下:"
#         print userRecommendList
        
        ####user的喜欢列表
        userLikeLsit = []
        for data in ProbeSetData:
            if int(data[0]) == int(user)+1:
                userLikeLsit.append(data[1])
#         print "USER_ID为"+str(user)+"的喜欢列表如下:"
#         print userLikeLsit
        ####user的购买列表
        userbuylist = []
        for data in TrainSetData:
            if int(data[0] == int(user)+1):
                userbuylist.append(data[1])
#         print "USER_ID为"+str(user)+"的购买列表如下:"
#         print userbuylist
        #计算user召回率        #计算user推荐准确率
        if userLikeLsit:        
            userLikeNum = 0
            userRecallList = []
            userRSgrade = []
            userAUCgrade = []
            
            userLikeQualityList = []
            
            userLikeRsList = [] 
            for likeID in userLikeLsit:
                for reList in userRecommendList:
                    if int(likeID)-1 == int(reList[0]):
                        userRecallList.append(likeID)
                        userLikeNum += 1
                for rsQuList in userRsRecommendList:
                    if int(likeID)-1 == int(rsQuList[0]):
                        tempLikeRsList = [int(index)+1 for index,x in enumerate(userRsRecommendList) if x[1] == rsQuList[1]]
    #                     print '该item'+str(likeID)+'的排名列表'+str(tempLikeRsList)
                        userLikeRsList.append((float(sum(tempLikeRsList))/len(tempLikeRsList))/len(userLikeLsit))
    #                     print '该item'+str(likeID)+'的平均排名'+str(float(sum(tempLikeRsList))/len(tempLikeRsList))
                likeIDQuality = [userQualityList[index] for index,x in enumerate(userQualityList) if x[0] == likeID-1][0]
                userLikeQualityList.append(likeIDQuality)
#             print "USER_ID为"+str(user)+"的喜欢物质量列表为如下:"    
#             print  userLikeQualityList
#             print "USER_ID为"+str(user)+"的召回列表为如下:"
#             print userRecallList
            userPrecision = float(userLikeNum)/Re_length
#             print "USER_ID为"+str(user)+"的推荐准确率为:"+str(userPrecision)
            Precision_List.append(userPrecision)
            userRecall = float(userLikeNum)/len(userLikeLsit)
#             print "USER_ID为"+str(user)+"的推荐召回率为:"+str(userRecall)
            Recall_List.append(userRecall)
#             print "该用户不相关的item长度为："+str(len(TrainSet_itemList)-len(userbuylist))
            userRSgrade = float(sum(userLikeRsList))/(len(TrainSet_itemList)-len(userbuylist))
#             print "USER_ID为"+str(user)+"的排名RS为:"+str(userRSgrade)
            RSgrade_List.append(userRSgrade)
        
            #计算AUC
            AUCgrade = 0
            for time in range(timeNum):
                randomUserQuality = random.choice(userQualityList)
                randomUserLike = random.choice(userLikeQualityList)
    #             randomLikeID = random.choice(userLikeLsit)
    #             randomUserLike = [userQualityList[index] for index,x in enumerate(userQualityList) if x[0]== randomLikeID][0]
                if randomUserQuality[1] > randomUserLike[1]:
                    AUCgrade += 0
                elif randomUserQuality[1] < randomUserLike[1]:
                    AUCgrade += 1
                else:
                    AUCgrade += 0.5
            userAUCgrade= float(AUCgrade)/timeNum
#             print "USER_ID为"+str(user)+"的推荐AUC为:"+str(userAUCgrade)
            AUCgrade_List.append(userAUCgrade)
#         else:
#             print "USER_ID没有喜欢列表"
        #user += 1
    count += 1
    Params = float(Params) - 0.1
        
    Precision = sum(Precision_List)/len(ProbeSet_userList)
    print "推荐算法的平均准确率是："+str(Precision)    
    Recall = sum(Recall_List)/len(ProbeSet_userList)
    print "推荐算法的平均召回率是："+str(Recall)
    F1 = float(2*Precision*Recall)/(Precision+Recall)
    print "推荐算法的F1指标为："+str(F1)
    RS = sum(RSgrade_List)/len(ProbeSet_userList)
    print "推荐算法的推荐准确度是："+str(RS)
    AUCgrade = sum(AUCgrade_List)/len(ProbeSet_userList)
    print "推荐算法的推荐AUC是："+str(AUCgrade)


