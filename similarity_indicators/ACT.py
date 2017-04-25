#coding=UTF-8
'''
Created on Nov 29, 2016

@author: ZWT
'''
import numpy as np
import time

def ACT(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    Matrix_D = np.diag(sum(MatrixAdjacency_Train))
    Matrix_Laplacian = Matrix_D - MatrixAdjacency_Train
    INV_Matrix_Laplacian  = np.linalg.pinv(Matrix_Laplacian)
    
    Array_Diag = np.diag(INV_Matrix_Laplacian)
    Matrix_ONE = np.ones([MatrixAdjacency_Train.shape[0],MatrixAdjacency_Train.shape[0]])
    Matrix_Diag = Array_Diag * Matrix_ONE

    Matrix_similarity = Matrix_Diag + Matrix_Diag.T - (2 * Matrix_Laplacian)
    print Matrix_similarity
    Matrix_similarity = Matrix_ONE / Matrix_similarity
    Matrix_similarity = np.nan_to_num(Matrix_similarity)
    
    similarity_EndTime = time.clock()
    print "    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)
    return Matrix_similarity