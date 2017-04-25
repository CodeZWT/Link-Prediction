#coding=UTF-8
'''
Created on Nov 29, 2016

@author: ZWT
'''
import numpy as np
import time

def RWR(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    Parameter = 0.85
    
    Matrix_TransitionProbobility = MatrixAdjacency_Train / sum(MatrixAdjacency_Train)
    Matrix_EYE = np.eye(MatrixAdjacency_Train.shape[0])
    
    Temp = Matrix_EYE - Parameter * Matrix_TransitionProbobility.T
    INV_Temp = np.linalg.inv(Temp)
    Matrix_RWR = (1 - Parameter) * np.dot(INV_Temp,Matrix_EYE)
    Matrix_similarity = Matrix_RWR + Matrix_RWR.T
    
    
    similarity_EndTime = time.clock()
    print "    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)
    return Matrix_similarity
