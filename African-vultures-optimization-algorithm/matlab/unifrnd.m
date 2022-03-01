function [m] = unifrnd(lb,ub,x,y)
    m = rand(x,y) * (ub - lb) + lb
end