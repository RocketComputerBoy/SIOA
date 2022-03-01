# Generated with SMOP  0.41
#from libsmop import *
# initialization.m

    # This function initialize the first population of search agents
    
from numpy import *
from numpy.random import *
#@function
def initialization(N=None,dim=None,ub=None,lb=None,*args,**kwargs):
    #isList = type(ub) == list
    X = zeros((N,dim))
    Boundary_no=size(array(ub),0)
    '''if isList:
        Boundary_no=size(array(ub),0)
    else:
        Boundary_no=size(array([ub]),0)'''
# initialization.m:4
    
    # If the boundaries of all variables are equal and user enter a signle
# number for both ub and lb
    if Boundary_no == 1:
        X=multiply(rand(N,dim),(ub - lb)) + lb
# initialization.m:9
    # If each variable has a different lb and ub
    if Boundary_no > 1:
        for i in arange(1,dim).reshape(-1):
            ub_i=ub[i]
# initialization.m:15
            lb_i=lb[i]
# initialization.m:16
            qq=multiply(rand(N,1),(ub_i - lb_i)) + lb_i
            #print('qq:',qq.shape)
            X[:,i]=(multiply(rand(N,1),(ub_i - lb_i)) + lb_i).reshape(N,)
    return X
# initialization.m:17
    
