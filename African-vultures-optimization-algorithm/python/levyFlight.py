# Generated with SMOP  0.41
#from libsmop import *
# levyFlight.m

from numpy import *
from scipy.special import gamma
from numpy.random import *
#@function
def levyFlight(d=None,*args,**kwargs):
#    varargin = levyFlight.varargin
#    nargin = levyFlight.nargin

    
    beta=3 / 2
# levyFlight.m:3
    sigma=(dot(gamma(1 + beta),sin(dot(pi,beta) / 2)) / (dot(dot(gamma((1 + beta) / 2),beta),2 ** ((beta - 1) / 2)))) ** (1 / beta)
# levyFlight.m:5
    u=dot(randn(1,d),sigma)
# levyFlight.m:6
    v=randn(1,d)
# levyFlight.m:7
    step=u / abs(v) ** (1 / beta)
# levyFlight.m:8
    o=copy(step)
# levyFlight.m:10
    return o
    
if __name__ == '__main__':
    pass
    
