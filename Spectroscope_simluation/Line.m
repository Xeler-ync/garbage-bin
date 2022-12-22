classdef Line
    properties
        A = 0.0;
        B = 0.0;
        C = 0.0;
        k = 0.0;
        b = 0.0;
    end

    methods
        function obj = Line(A_, B_, C_)
            obj.A = A_;
            obj.B = B_;
            obj.C = C_;
            if ~isnan(A_) && ~isnan(B_) && ~isnan(C_)
                obj = obj.ABC2kb();
            end
        end

        function obj = ReflashBykb(obj, k_, b_)
            obj.k = k_;
            obj.b = b_;
            obj = obj.kb2ABC();
        end

        function obj = ReflashByTwoPoint(obj, point1_, point2_)
            obj.A = point2_.y - point1_.y;
            obj.B = point1_.x - point2_.x;
            obj.C = point2_.x * point1_.y - point1_.x * point2_.y;
            obj = obj.ABC2kb();
        end

        function obj = ReflashByLine(obj, line_)
            obj.A = line_.A;
            obj.B = line_.B;
            obj.C = line_.C;
            obj.k = line_.k;
            obj.b = line_.b;
        end

        function obj = ReflashBykPoint(obj, k_, point_)
            obj = obj.ReflashBykb(k_, (point_.y - k_*point_.x));
        end

        function obj = ABC2kb(obj)
            obj.k = -obj.A / obj.B;
            obj.b = -obj.C / obj.B;
        end

        function obj = kb2ABC(obj)
            obj.A = obj.k;
            obj.B = -1;
            obj.C = obj.b;
        end

        %% get x from ABCy
        function x_ = GetxFromABCy(obj, y_)
            x_ = (-obj.C - obj.B*y_) / obj.A;
        end

        %% get y from ABCx
        function y_ = GetyFromABCx(obj, x_)
            y_ = (-obj.C - obj.A*x_) / obj.B;
        end

        function is_on_ = PointIsOn(obj, point_)
            is_on_ = point_.x == obj.GetxFromABCy(point_.y);
        end

        function point_ = GetCrossPoint(obj, line_)
            point_ = Point_( ...
                ((-obj.C) * line_.B - obj.B * (-line_.C)) / (obj.A * line_.B - obj.B * line_.A), ...
                (obj.A * (-line_.C) - (-obj.C) * line_.A) / (obj.A * line_.B - obj.B * line_.A) ...
            );
        end
    end
end