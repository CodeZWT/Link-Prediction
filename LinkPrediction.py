#coding=UTF-8
'''
Created on 2016��11��20��

@author: ZWT
'''
import time
import os
import Initialize
import Evaluation_Indicators.AUC


import similarity_indicators.CommonNeighbor
import similarity_indicators.Salton
import similarity_indicators.Jaccard
import similarity_indicators.Sorenson
import similarity_indicators.HPI
import similarity_indicators.HDI
import similarity_indicators.LHN_I
import similarity_indicators.PA
import similarity_indicators.AA
import similarity_indicators.RA

import similarity_indicators.LP
import similarity_indicators.Katz

import similarity_indicators.ACT
import similarity_indicators.Cos

startTime = time.clock()
#初始化训练测试集合
READEME1 = '''Please choose a Set:
    PPI            1
    NS             2
    Grid           3
    PB             4
    INT            5
    USAir          6'''
print READEME1
Set = int(raw_input('Input Set:'))
if Set == 1:
    NetFile = u'Data/PPI.txt'
    NetName = 'PPI'
elif Set == 2:
    NetFile = u'Data/NS.txt'
    NetName = 'NS'
elif Set == 3:
    NetFile = u'Data/Grid.txt'
    NetName = 'Grid'
elif Set == 4:
    NetFile = u'Data/PB.txt'
    NetName = 'PB'
elif Set == 5:
    NetFile = u'Data/INT.txt'
    NetName = 'INT'
elif Set == 6:
    NetFile = u'Data/USAir.txt'
    NetName = 'USAir'
else:
    print 'Input Error'
     
print "\nLink Prediction start：\n"
TrainFile_Path = 'Data\\'+NetName+'\\Train.txt'
if os.path.exists(TrainFile_Path):
    Train_File = 'Data\\'+NetName+'\\Train.txt'
    Test_File = 'Data\\'+NetName+'\\Test.txt'
    MatrixAdjacency_Train,MatrixAdjacency_Test,MaxNodeNum = Initialize.Init2(Test_File, Train_File)
else:
    MatrixAdjacency_Net,MaxNodeNum = Initialize.Init(NetFile)
    MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)

#计算相似性矩阵
# READEME = '''\nPlease choose a method:
#     CN            0
#     Salton        1
#     Jaccard       2
#     Sorenson      3
#     HPI           4
#     HDI           5
#     LHN-I         6
#     PA            7
#     AA            8
#     RA            9
#     LP            10
#     Katz          11
#     ACT           12
#     RWR           13'''
# print READEME
# Method = int(raw_input('Input Method:'))
similarity_StartTime = time.clock()

# Matrix_similarity = similarity_indicators.Cos.ACT(MatrixAdjacency_Train)

for Method in range(14):
    if Method == 0:
        print '----------SIM----------基于局部信息----------SIM----------'
        print '----------Cn----------'
        Matrix_similarity = similarity_indicators.CommonNeighbor.Cn(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 1:
        print '----------Salton----------'
        Matrix_similarity = similarity_indicators.Salton.Salton(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 2:
        print '----------Jaccard----------'
        Matrix_similarity = similarity_indicators.Jaccard.Jaccavrd(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 3:
        print '----------Sorenson----------'
        Matrix_similarity = similarity_indicators.Sorenson.Sorenson(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 4:
        print '----------HPI----------'
        Matrix_similarity = similarity_indicators.HPI.HPI(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 5:
        print '----------HDI----------'
        Matrix_similarity = similarity_indicators.HDI.HDI(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 6:
        print '----------LHN-1----------'
        Matrix_similarity = similarity_indicators.LHN_I.LHN_I(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 7:
        print '----------PA----------'
        Matrix_similarity = similarity_indicators.PA.PA(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 8:
        print '----------AA----------'
        Matrix_similarity = similarity_indicators.AA.AA(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 9:
        print '----------RA----------'
        Matrix_similarity = similarity_indicators.RA.RA(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 10:
        print '----------SIM----------基于路径----------SIM----------'
        print '----------LP----------'
        Matrix_similarity = similarity_indicators.LP.LP(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 11:
        print '----------Katz----------'
        Matrix_similarity = similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 12:
        print '----------SIM----------基于随机游走----------SIM----------'
        print '----------ACT----------'
        Matrix_similarity = similarity_indicators.ACT.ACT(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    elif Method == 13:
        print '----------Cos----------'
        Matrix_similarity = similarity_indicators.Cos.Cos(MatrixAdjacency_Train)
        Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    else:
        print "Method Error!"
        
similarity_EndTime = time.clock()
print '----------！！----------'
print "All SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)

# #计算auc
Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)

endTime = time.clock()
print "\nRunTime: %f s" % (endTime - startTime)