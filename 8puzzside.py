# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:51:20 2024

@author: 21pt26
"""
import sys
visited=[]
path=[]
def getindex(m,e):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==e:
                return i,j
def manhattandist(mat):
    s=0
    for i in range(1,9):
        gx,gy=getindex([[0,1,2],[3,4,5],[6,7,8]],i)
        x,y=getindex(mat,i)
        s+=(abs(gx-x)+abs(gy-y))
    return s
def find_key_by_value(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    return None
      
    
def swap(a, matrix, lis):
    matrix_copy = [row[:] for row in matrix]  
    i, j = lis[0], lis[1]
    if a == 'L' and j != 0:
        matrix_copy[i][j], matrix_copy[i][j - 1] = matrix_copy[i][j - 1], matrix_copy[i][j]
    elif a == 'R' and j != (len(matrix_copy) - 1):
        matrix_copy[i][j], matrix_copy[i][j + 1] = matrix_copy[i][j + 1], matrix_copy[i][j]
    elif a == 'U' and i != 0:
        matrix_copy[i - 1][j], matrix_copy[i][j] = matrix_copy[i][j], matrix_copy[i - 1][j]
    elif a == 'D' and i != (len(matrix_copy) - 1):
        matrix_copy[i][j], matrix_copy[i + 1][j] = matrix_copy[i + 1][j], matrix_copy[i][j]
    else:
        return None
    return matrix_copy

def gen_graph(lis_str):
    if lis_str==[[0,1,2],[3,4,5],[6,7,8]]:
        sys.exit(0)
        return True
        
    for i in range(len(lis_str)):
        for j in range(len(lis_str[i])):
            if lis_str[i][j]==0:
                pos=[i,j]

    visited.append(lis_str)

    v1=swap('U',lis_str,pos)
    v2=swap('D',lis_str,pos)
    v3=swap('R',lis_str,pos)
    v4=swap('L',lis_str,pos)
    suc=[]
    if v1 and v1 not in visited:
        suc.append(v1)
    if v2 and v2 not in visited:
        suc.append(v2)
    if v3 and v3 not in visited:
        suc.append(v3)
    if v4 and v4 not in visited:
        suc.append(v4)
    if not suc==[]:
        score={}
        for i in range(len(suc)):
            score[int(i+1)]=manhattandist(suc[i])
        val=list(score.values())
        next_child=find_key_by_value(score, min(val))
        g=suc[next_child-1]
        """if manhattandist(g)>manhattandist(lis_str):
            print(g,manhattandist(g))
            print(lis_str,manhattandist(lis_str))
            return False
        else:"""
        print(g)
        path.append(g)
        gen_graph(g)
gen_graph([[7,2,4],[5,0,6],[8,3,1]])
