#coding=UTF-8
'''
Created on 2016��11��19��

@author: ZWT
'''
import numpy as np
import time
def Calculation_AUC(MatrixAdjacency_Train,MatrixAdjacency_Test,Matrix_similarity,MaxNodeNum):
    AUC_TimeStart = time.clock()
    print '    Calculation AUC......'
    AUCnum = 672400
    
    Matrix_similarity = np.triu(Matrix_similarity - Matrix_similarity * MatrixAdjacency_Train)
    Matrix_NoExist = np.ones(MaxNodeNum) - MatrixAdjacency_Train - MatrixAdjacency_Test - np.eye(MaxNodeNum)
     
    Test = np.triu(MatrixAdjacency_Test)
    NoExist = np.triu(Matrix_NoExist)
    
#     Test_num =len(np.argwhere(Test == 1))
#     NoExist_num = len(np.argwhere(NoExist == 1))
# # #   Test_num = np.nonzero(Test)[0].shape[0]
# # #   NoExist_num = np.nonzero(NoExist)[0].shape[0]

    Test_num = len(np.argwhere(Test == 1))
    NoExist_num = len(np.argwhere(NoExist == 1))
#     print '    Test_num：%d'%Test_num
#     print '    NoExist_num：%d'%NoExist_num
      
    Test_rd = [int(x) for index,x in enumerate((Test_num * np.random.rand(1,AUCnum))[0])]
    NoExist_rd = [int(x) for index,x in enumerate((NoExist_num * np.random.rand(1,AUCnum))[0])]
#     print '    Test_rd：'+str(Test_rd)
#     print '    Test_rd长度：'+str(len(Test_rd))
#     print '    Test_rd最大值：'+str(max(Test_rd))
#     print '    NoExist_rd：'+str(NoExist_rd)
#     print '    NoExist_rd长度：'+str(len(NoExist_rd))
    TestPre= Matrix_similarity * Test
    NoExistPre = Matrix_similarity * NoExist
    
    TestIndex = np.argwhere(Test == 1)
    Test_Data = np.array([TestPre[x[0],x[1]] for index,x in enumerate(TestIndex)]).T
    NoExistIndex = np.argwhere(NoExist == 1)
    NoExist_Data = np.array([NoExistPre[x[0],x[1]] for index,x in enumerate(NoExistIndex)]).T
#     print Test_Data
#     print Test_Data.shape
#     print NoExist_Data
#     print NoExist_Data.shape
    
    Test_rd = np.array([Test_Data[x] for index,x in enumerate(Test_rd)])
    NoExist_rd = np.array([NoExist_Data[x] for index,x in enumerate(NoExist_rd)])
#     print Test_rd
#     print Test_rd.shape
#     print NoExist_rd
#     print NoExist_rd.shape

#     aucArray = Test_rd - NoExist_rd
#     n1 = len(np.argwhere(aucArray > 0))
#     n2 = len(np.argwhere(aucArray == 0))
    n1,n2 = 0,0
    for num in range(AUCnum):
        if Test_rd[num] > NoExist_rd[num]:
            n1 += 1
        elif Test_rd[num] == NoExist_rd[num]:
            n2 += 0.5
        else:
            n1 += 0
    auc = float(n1+n2)/AUCnum
    print '    AUC指标为：%f'%auc
    AUC_TimeEnd = time.clock()
    print '    AUCTime：%f s'%(AUC_TimeEnd - AUC_TimeStart)
    return auc