# Generated with SMOP  0.41
#from libsmop import *
# exploration.m

    
from numpy.random import *
from numpy import *
#@function
def exploration(current_vulture_X=None,random_vulture_X=None,F=None,p1=None,upper_bound=None,lower_bound=None,*args,**kwargs):
#    varargin = exploration.varargin
#    nargin = exploration.nargin

    if rand() < p1:
        current_vulture_X=random_vulture_X-(abs((2*rand())*random_vulture_X-current_vulture_X))*F
        #current_vulture_X=random_vulture_X - dot((abs(dot((dot(2,rand())),random_vulture_X) - current_vulture_X)),F)
# exploration.m:4
    else:
        current_vulture_X=(random_vulture_X - (F) + dot(rand(),(dot((upper_bound - lower_bound),rand()) + lower_bound)))
# exploration.m:6
    
    
    return current_vulture_X
    
if __name__ == '__main__':
    pass
    
