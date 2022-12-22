classdef Point_
    properties
        x;
        y;
    end

    methods
        function obj = Point_(x_, y_)
            obj.x = x_;
            obj.y = y_;
        end

        function dis = getDistance(obj, point_)
            dis = ((obj.x - point_.x) ^ 2 + (obj.y - point_.y) ^ 2) ^ .5;
        end

        function obj = move(obj, x_move_, y_move_)
            obj.x = obj.x + x_move_;
            obj.y = obj.y + y_move_;
        end

        function is_eq_ = eq(obj, ipt_)
            is_eq_ = (obj.x == ipt_.x) && (obj.y == ipt_.y);
        end
    end
end