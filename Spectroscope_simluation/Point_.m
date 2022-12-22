classdef Point_
    properties
        x = 0.0;
        y = 0.0;
    end

    methods
        function obj = Point_(x_, y_)
            obj.x = x_;
            obj.y = y_;
        end

        function obj = move(obj, x_move_, y_move_)
            obj.x = obj.x + x_move_;
            obj.y = obj.y + y_move_;
        end
    end
end