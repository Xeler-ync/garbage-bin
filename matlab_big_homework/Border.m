classdef Border < Rectangle
    properties
    end

    methods
        function obj = Border(x1_, x2_, y1_, y2_)
            obj = obj@Rectangle(x1_, x2_, y1_, y2_);
        end

        function isImpact_ = isBallImpact(obj, ball_)
            isImpact_ = ~((min(obj.x1, obj.x2) <= (ball_.position.x - ball_.radius)) && ...
                          (max(obj.x1, obj.x2) >= (ball_.position.x + ball_.radius)) && ...
                          (min(obj.y1, obj.y2) <= (ball_.position.y - ball_.radius)) && ...
                          (max(obj.y1, obj.y2) >= (ball_.position.y + ball_.radius)));
        end

        function direction_ = ballImpactDirection(obj, ball_)
            direction_ = "";
            if min(obj.x1, obj.x2) > ball_.position.x - ball_.radius
                direction_ = direction_ + "l";
            end
            if max(obj.x1, obj.x2) < ball_.position.x + ball_.radius
                direction_ = direction_ + "r";
            end
            if min(obj.y1, obj.y2) > ball_.position.y - ball_.radius
                direction_ = direction_ + "b";
            end
            if max(obj.y1, obj.y2) < ball_.position.y + ball_.radius
                direction_ = direction_ + "t";
            end
        end

        function ball_ = impactBall(~, ball_, direction_)
            if contains(direction_, "l")
                if ball_.speed.x < 0
                    ball_.speed.x = +abs(ball_.speed.x) * 0.5;
                end
            end
            if contains(direction_, "r")
                if ball_.speed.x > 0
                    ball_.speed.x = -abs(ball_.speed.x) * 0.5;
                end
            end
            if contains(direction_, "b")
                if ball_.speed.y < 0
                    ball_.speed.y = +abs(ball_.speed.y) * 0.5;
                end
            end
            if contains(direction_, "t")
                if ball_.speed.y > 0
                    ball_.speed.y = -abs(ball_.speed.y) * 0.5;
                end
            end
        end
    end
end