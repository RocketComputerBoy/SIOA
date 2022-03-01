# Generated with SMOP  0.41
#from libsmop import *
# random_select.m
from rouletteWheelSelection import rouletteWheelSelection
#@function
def random_select(Best_vulture1_X=None,Best_vulture2_X=None,alpha=None,betha=None,*args,**kwargs):
 #   varargin = random_select.varargin
  #  nargin = random_select.nargin

    probabilities=[alpha,betha]
# random_select.m:3
    if (rouletteWheelSelection(probabilities) == 1):
        random_vulture_X=Best_vulture1_X
# random_select.m:6
    else:
        random_vulture_X=Best_vulture2_X
# random_select.m:8
    
    return random_vulture_X
    
if __name__ == '__main__':
    pass
    
