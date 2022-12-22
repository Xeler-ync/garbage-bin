classdef CirclePeriod < Circle
    properties
        range = Range_(0, 0);
    end

    methods
        function obj = CirclePeriod(center_, radius_, range_)
            obj = obj@Circle(center_, radius_);
            obj.range = range_;
        end
    end
end