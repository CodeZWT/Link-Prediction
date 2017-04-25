#coding=UTF-8
'''
Created on 2016��11��24��

@author: ZWT
'''
import numpy as np
import time

def Sorenson(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train)

    deg_row = sum(MatrixAdjacency_Train)
    deg_row.shape = (deg_row.shape[0],1)
    deg_row_T = deg_row.T
    tempdeg = deg_row + deg_row_T
    
    Matrix_similarity = (2 * Matrix_similarity) / tempdeg
    
    similarity_EndTime = time.clock()
    print "    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)
    return Matrix_similarity
# import numpy.matlib as matlab
# def Sorenson(MatrixAdjacency_Train):
#     Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train)
# 
#     Matrix_similarity = np.triu(Matrix_similarity, 1)
#     
#     deg_col = matlab.repmat((matlab.sum(MatrixAdjacency_Train,1)), 1, matlab.size(MatrixAdjacency_Train, 1))
#     print deg_col.shape
#     deg_col_T = deg_col.T
#     deg_col = deg_col_T + deg_col
#     deg_col = np.triu(deg_col)
#     
#     Matrix_similarity = (2 * Matrix_similarity) / deg_col 
# 
#     return Matrix_similarity