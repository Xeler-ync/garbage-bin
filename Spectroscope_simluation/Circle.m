classdef Circle
    properties
        center = Point_(0.0, 0.0);
        radius = 0;
    end

    methods
        function obj = Circle(center_, radius_)
            obj.center = center_;
            obj.radius = radius_;
        end
    end
end