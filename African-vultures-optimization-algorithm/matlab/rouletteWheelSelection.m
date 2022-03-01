function [index] = RouletteWheelSelection(x)

    index=find(rand(1) <= cumsum(x) ,1,'first');

end
