classdef Range_
    properties
        lower = 0.0
        upper = 0.0
    end

    methods
        function obj = Range_(lower_, upper_)
            obj.lower = lower_;
            obj.upper = upper_;
        end
    end
end