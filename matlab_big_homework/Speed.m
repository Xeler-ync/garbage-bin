classdef Speed
    properties
        x;
        y;
    end

    methods
        function obj = Speed(x_, y_)
            obj.x = x_;
            obj.y = y_;
        end

        function v_ = getResultantSpeed(obj)
            v_ = (obj.x ^ 2 + obj.y ^ 2) ^ .5;
        end

        function relativeSpeed_ = getRelativeSpeed(obj, iptSpeed_)
            relativeSpeed_ = Speed(obj.x - iptSpeed_.x, obj.y - iptSpeed_.y);
        end

        function obj = increaseSpeed(obj, x_, y_)
            obj.x = obj.x + x_;
            obj.y = obj.y + y_;
        end

        function is_eq_ = eq(obj, ipt_)
            is_eq_ = (obj.x == ipt_.x) && (obj.y == ipt_.y);
        end
    end
end