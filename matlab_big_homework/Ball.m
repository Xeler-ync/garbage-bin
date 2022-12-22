classdef Ball
    properties
        speed; % Speed
        position; % Point_
        mass;
        radius;
    end

    methods
        function obj = Ball(speed_, position_, mass_, radius_)
            obj.speed = speed_;
            obj.position = position_;
            obj.mass = mass_;
            obj.radius = radius_;
        end

        function isImpact_ = isBallImpact(obj, ball_)
            isImpact_ = obj.radius + ball_.radius >= obj.position.getDistance(ball_.position);
        end

        function obj = moveTimePeriod(obj, time_period_)
            obj.position = obj.position.move(obj.speed.x * time_period_, obj.speed.y * time_period_);
        end

        function [this_, that_] = impactBall(obj, that_)
            this_ = obj;
            dx = that_.position.x - this_.position.x;
            dy = that_.position.y - this_.position.y;
            angle_ = atan2(dy, dx);
            sin_ = sin(angle_);
            cos_ = cos(angle_);

            vx0 = this_.speed.x * cos_ + this_.speed.y * sin_;
            vy0 = this_.speed.y * cos_ - this_.speed.x * sin_;
            vx1 = that_.speed.x * cos_ + that_.speed.y * sin_;
            vy1 = that_.speed.y * cos_ - that_.speed.x * sin_;

            vx_total = vx0 - vx1;
            % prevent repeated collisions
            if sign(dx) == sign(vx_total)
                distance = this_.position.getDistance(that_.position);
                if (distance < max(this_.radius/2, this_.radius-2)) || (distance < max(that_.radius/2, that_.radius-2))
                    % force pop when too close
                    vx0 = sign(dx) * abs(vx0);
                    vx1 = -sign(dx) * abs(vx_total + vx0);
                else
                    return;
                end
            else
                vx0 = ((this_.mass - that_.mass) * vx0 + 2 * that_.mass * vx1) / (this_.mass + that_.mass);
                vx1 = vx_total + vx0;
            end

            this_speed_y = vy0 * cos_ + vx0 * sin_;
            that_speed_y = vy1 * cos_ + vx1 * sin_;
            if abs(this_speed_y) < 1e-14
                this_speed_y = 0;
            end
            if abs(that_speed_y) < 1e-14
                that_speed_y = 0;
            end

            this_.speed.x = vx0 * cos_ - vy0 * sin_;
            this_.speed.y = this_speed_y;
            that_.speed.x = vx1 * cos_ - vy1 * sin_;
            that_.speed.y = that_speed_y;
        end

        function obj = speedEnthreshold(obj, speed_)
            resultant_speed = obj.speed.getResultantSpeed;
            if obj.speed.getResultantSpeed > speed_
                obj.speed.x = obj.speed.x * speed_ / resultant_speed;
                obj.speed.y = obj.speed.y * speed_ / resultant_speed;
            end
        end

        function is_eq_ = eq(obj, ipt_)
            is_eq_ = (obj(1).speed == ipt_.speed) && ...
                     (obj(1).position == ipt_.position) && ...
                     (obj(1).mass == ipt_.mass) && ...
                     (obj(1).radius == ipt_.radius);
        end
    end
end