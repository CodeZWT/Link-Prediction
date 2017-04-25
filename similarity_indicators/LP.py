#coding=UTF-8
'''
Created on Nov 29, 2016

@author: ZWT
'''

import numpy as np
import time

def LP(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train)
    
    Parameter = 1
    Matrix_LP = np.dot(np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train),MatrixAdjacency_Train) * Parameter
    
    Matrix_similarity = np.dot(Matrix_similarity,Matrix_LP)
    similarity_EndTime = time.clock()
    print "    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)
    return Matrix_similarity
