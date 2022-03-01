# Generated with SMOP  0.41

# AVOA.m

    
from numpy import *
from numpy.random import *
from initialization import initialization
from boundaryCheck import boundaryCheck
from random_select import random_select
from exploration import exploration
from exploitation import exploitation

unifrnd=uniform
def AVOA(pop_size=None,max_iter=None,lower_bound=None,upper_bound=None,variables_no=None,fobj=None,*args,**kwargs):
    upper_bound = array(upper_bound)
    lower_bound = array(lower_bound)
    # initialize Best_vulture1, Best_vulture2
    Best_vulture1_X=zeros((1,variables_no))
# AVOA.m:5
    Best_vulture1_F=copy(inf)
# AVOA.m:6
    Best_vulture2_X=zeros((1,variables_no))
# AVOA.m:7
    Best_vulture2_F=copy(inf)
# AVOA.m:8
    
    X=initialization(pop_size,variables_no,upper_bound,lower_bound)
# AVOA.m:11
   # print('X=',X) 
    p1=0.6
# AVOA.m:14
    p2=0.4
# AVOA.m:15
    p3=0.6
# AVOA.m:16
    alpha=0.8
# AVOA.m:17
    betha=0.2
# AVOA.m:18
    gamma=2.5
# AVOA.m:19
    convergence_curve = []
    current_iter=0
# AVOA.m:22
    
    while current_iter < max_iter:

        for i in arange(1,size(array(X),0)).reshape(-1):
            # Calculate the fitness of the population
            current_vulture_X=X[i,:]
# AVOA.m:27
            current_vulture_F=fobj(current_vulture_X)
# AVOA.m:28
            if current_vulture_F < Best_vulture1_F:
                Best_vulture1_F=copy(current_vulture_F)
# AVOA.m:32
                Best_vulture1_X=copy(current_vulture_X)
# AVOA.m:33
            if current_vulture_F > Best_vulture1_F and current_vulture_F < Best_vulture2_F:
                Best_vulture2_F=copy(current_vulture_F)
# AVOA.m:36
                Best_vulture2_X=copy(current_vulture_X)
# AVOA.m:37
        a=dot(unifrnd(- 2,2,(1,1)),((sin(dot((pi / 2),(current_iter / max_iter))) ** gamma) + cos(dot((pi / 2),(current_iter / max_iter))) - 1))
# AVOA.m:41
        P1=dot((dot(2,rand()) + 1),(1 - (current_iter / max_iter))) + a
# AVOA.m:42
        #print('att:',arange(1, size(array(X),0)))
        for i in arange(1,size(array(X),0)).reshape(-1):
            current_vulture_X=X[i,:]
# AVOA.m:46
            F=dot(P1,(dot(2,rand()) - 1))
            #print('F=',F)
# AVOA.m:47
            random_vulture_X=random_select(Best_vulture1_X,Best_vulture2_X,alpha,betha)
# AVOA.m:49
            if abs(F) >= 1:
                current_vulture_X=exploration(current_vulture_X,random_vulture_X,F,p1,upper_bound,lower_bound)
                #print('F>=1')
# AVOA.m:52
            else:
                if abs(F) < 1:
                    #print('F<1')
                    current_vulture_X=exploitation(current_vulture_X,Best_vulture1_X,Best_vulture2_X,random_vulture_X,F,p2,p3,variables_no,upper_bound,lower_bound)
# AVOA.m:54
            X[i,:]=current_vulture_X
# AVOA.m:57
        current_iter=current_iter + 1
# AVOA.m:60
       # convergence_curve[current_iter]=Best_vulture1_F
# AVOA.m:61
        X=boundaryCheck(X,lower_bound,upper_bound)
        convergence_curve.append(Best_vulture1_F)
# AVOA.m:63
        print('In Iteration %d, best estimation of the global optimum is %f'%(current_iter,Best_vulture1_F))
        print('best x :',Best_vulture1_X,'\n')

    
    return Best_vulture1_F,Best_vulture1_X,convergence_curve
    
if __name__ == '__main__':
    pass
    
