#coding=UTF-8
'''
Created on Nov 30, 2016

@author: ZWT
'''
import numpy as np
import time

# def Cos(MatrixAdjacency_Train):
#     similarity_StartTime = time.clock()
#     
#     Matrix_D = np.diag(sum(MatrixAdjacency_Train))
#     Matrix_D.shape = (Matrix_D.shape[0],1)
#     Matrix_Laplacian = Matrix_D - MatrixAdjacency_Train
#     INV_Matrix_Laplacian  = np.linalg.pinv(Matrix_Laplacian)
#     
#     Array_Diag = np.diag(INV_Matrix_Laplacian)
#     Matrix_ONE = np.ones([MatrixAdjacency_Train.shape[0],MatrixAdjacency_Train.shape[0]])
# 
#     Matrix_similarity = (Matrix_D.T,Matrix_D)
#     print Matrix_similarity
#     Matrix_similarity = np.sqrt(Matrix_similarity)
#     print Matrix_similarity
#     Matrix_similarity = INV_Matrix_Laplacian / Matrix_similarity
#     Matrix_similarity
#     Matrix_similarity = np.nan_to_num(Matrix_similarity)
#     
#     similarity_EndTime = time.clock()
#     print "    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)
#     return Matrix_similarity

def Cos(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
     
    Matrix_D = np.diag(sum(MatrixAdjacency_Train))
    Matrix_Laplacian = Matrix_D - MatrixAdjacency_Train
    INV_Matrix_Laplacian  = np.linalg.pinv(Matrix_Laplacian)
     
    Array_Diag = np.diag(INV_Matrix_Laplacian)
    Matrix_ONE = np.ones([MatrixAdjacency_Train.shape[0],MatrixAdjacency_Train.shape[0]])
    Matrix_Diag = Array_Diag * Matrix_ONE
 
    Matrix_similarity = INV_Matrix_Laplacian/((Matrix_Diag * Matrix_Diag.T) ** 0.5)
    print Matrix_similarity
    Matrix_similarity = np.nan_to_num(Matrix_similarity)
     
    similarity_EndTime = time.clock()
    print "    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)
    return Matrix_similarity