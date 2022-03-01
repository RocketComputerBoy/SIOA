# Generated with SMOP  0.41
#from libsmop import *
# boundaryCheck.m
from numpy import *
    
#@function
def boundaryCheck(X=None,lb=None,ub=None,*args,**kwargs):
    #varargin = BoundaryCheck.varargin
    #L::nargin = BoundaryCheck.nargin

    for i in arange(1,size(array([X]),0)).reshape(-1):
        FU=X(i,arange()) > ub
# boundaryCheck.m:4
        FL=X(i,arange()) < lb
# boundaryCheck.m:5
        X[i,arange()]=(multiply(X(i,arange()),(logical_not((FU + FL))))) + multiply(ub,FU) + multiply(lb,FL)
# boundaryCheck.m:6
    
    return X
    
if __name__ == '__main__':
    pass
    
