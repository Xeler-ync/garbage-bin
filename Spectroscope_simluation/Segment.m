classdef Segment < Line
    properties
        endpoint1 = Point_(0.0, 0.0);
        endpoint2 = Point_(0.0, 0.0);
    end

    methods
        function obj = Segment(endpoint1_, endpoint2_)
            obj = obj@Line(NaN,NaN,NaN);
            obj.endpoint1 = endpoint1_;
            obj.endpoint2 = endpoint2_;
            obj = obj.ReflashByTwoPoint(endpoint1_, endpoint2_);
        end

        function obj = ReflashByTwoPoint(obj, endpoint1, endpoint2)
            obj = ReflashByTwoPoint@Line(obj, endpoint1, endpoint2);
            obj.endpoint1 = endpoint1;
            obj.endpoint2 = endpoint2;
        end
    end
end