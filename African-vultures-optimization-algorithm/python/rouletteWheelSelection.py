# Generated with SMOP  0.41
#from libsmop import *
# rouletteWheelSelection.m

from numpy import *
from numpy.random import *
#@function
def rouletteWheelSelection(x=None,*args,**kwargs):
 #   varargin = RouletteWheelSelection.varargin
  #  nargin = RouletteWheelSelection.nargin
    #:rand = rand
    find = where
    index = find(rand() <= cumsum(x))[0]
# rouletteWheelSelection.m:3
    return index[0]
    
if __name__ == '__main__':
    pass
    
