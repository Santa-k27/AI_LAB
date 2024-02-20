# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:49:50 2024

@author: Santhosh_k27
"""

import sys
visited=[]
path=[]
def getindex(l,e):
    for i in range(len(l)):
        if l[i]==e:
                return i
def manhattan(st):
    s=0
    for i in range(len(st)):
        gx=getindex(['Y3','Y2','Y1','B','G1','G2','G3'],st[i])
        s+=(abs(gx-i))
    return s
def get_key(dictionary, value):
    for key,v in dictionary.items():
        if dictionary[key]==value:
            return key
    return None
def generate(oper,state,ind):
    copy_state=[]
    for i in range(len(state)):
        copy_state.append(state[i])
    if oper=='jump_adj_left' and ind!=0:
        copy_state[ind],copy_state[ind-1]=copy_state[ind-1],copy_state[ind]
    elif oper=='jump_adj_right' and ind!=(len(state)-1):
        copy_state[ind],copy_state[ind+1]=copy_state[ind+1],copy_state[ind]
    elif oper=='jump_over_left' and ind>1:
        copy_state[ind],copy_state[ind-2]=copy_state[ind-2],copy_state[ind]
    elif oper=='jump_over_right' and ind<(len(state)-2):
        copy_state[ind],copy_state[ind+2]=copy_state[ind+2],copy_state[ind]
    else:
        return None
    return copy_state


def frog_jump(state):
    if state==['Y1','Y2','Y3','B','G1','G2','G3']:
        print("the following frog can jump in ",len(path),"ways !!!")
        sys.exit(0)
        return True
    for i in range(len(state)):
            if state[i]=='B':
                pos=i
    visited.append(state)
    v1=generate('jump_adj_left',state,pos)
    v2=generate('jump_adj_right',state,pos)
    v3=generate('jump_over_left',state,pos)
    v4=generate('jump_over_right',state,pos)
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
            score[int(i+1)]=manhattan(suc[i])
        val=list(score.values())
        next_child=get_key(score, min(val))
        g=suc[next_child-1]
        print(g)
        path.append(g)
        frog_jump(g)
start=['G1','G2','G3','B','Y1','Y2','Y3']
frog_jump(start)