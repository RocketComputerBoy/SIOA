# Generated with SMOP  0.41
# main.m

    #African Vulture Optimization alghorithm
    
    # Read the following publication first and cite if you use it
    
    # @article{abdollahzadeh2021african,
#   title={African Vultures Optimization Algorithm: A New Nature-Inspired Metaheuristic Algorithm for Global Optimization Problems},
#   author={Abdollahzadeh, Benyamin and Gharehchopogh, Farhad Soleimanian and Mirjalili, Seyedali},
#   journal={Computers \& Industrial Engineering},
#   pages={107408},
#   year={2021},
#   publisher={Elsevier},
#   url = {https://www.sciencedirect.com/science/article/pii/S0360835221003120}
# }
from ObjectiveFunction import ObjectiveFunction
from AVOA import AVOA
from matplotlib.pyplot import *
from numpy import *
# Population size and stoppoing condition
pop_size=30
# main.m:21
max_iter=100
# main.m:22
    # Define your objective function's details here
fobj=ObjectiveFunction
# main.m:25
variables_no=2
# main.m:26
lower_bound=[-10 for i in range(variables_no)]
# main.m:27
    
upper_bound=[10 for i in range(variables_no)]
# main.m:28
    
    
Best_vulture1_F,Best_vulture1_X,convergence_curve=AVOA(pop_size,max_iter,lower_bound,upper_bound,variables_no,fobj,nargout=3)
print('best_y=',Best_vulture1_F)
print('best_x=',Best_vulture1_X)
iters = [it for it in range(max_iter)]
plot(iters, convergence_curve)
show()
# main.m:30
#figure
    # Best optimal values for the decision variables
#subplot(1,2,1)
#parallelcoords(Best_vulture1_X)
#xlabel('Decision variables')
#ylabel('Best estimated values ')
#box('on')
    # Best convergence curve
#subplot(1,2,2)
#plot(convergence_curve)
#title('Convergence curve of AVOA')
#xlabel('Current_iteration')
#ylabel('Objective value')
#box('on')
