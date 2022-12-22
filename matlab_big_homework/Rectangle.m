classdef Rectangle
    properties
        x1;
        x2;
        y1;
        y2;
    end

    methods
        function obj = Rectangle(x1_, x2_, y1_, y2_)
            obj.x1 = x1_;
            obj.x2 = x2_;
            obj.y1 = y1_;
            obj.y2 = y2_;
        end
    end
end