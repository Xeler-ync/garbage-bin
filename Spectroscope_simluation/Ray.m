classdef Ray < Line
    properties
        endpoint = Point_(0.0, 0.0);
        isNegetive = true;
        angle = 0.0;
    end

    methods
        function obj = Ray(A_, B_, C_ ,is_negetive_, endpoint_)
            obj = obj@Line(A_, B_, C_);
            obj.isNegetive = is_negetive_;
            obj.endpoint = endpoint_;
            if (~isnan(A_)) && (~isnan(B_)) && (~isnan(C_))
                try
                    obj = obj.iN2Angle();
                catch
                end
            end
        end

        function obj = ReflashByAngle(angle_)
            obj.angle = angle_;
            obj.Angle2iN();
        end

        %% make sure normal is forward to incident
        function obj = iN2Angle(obj)
            if isnan(obj.k)
                angle_ = NaN;
            else
                angle_ = atan(obj.k);
            end

            if (obj.isNegetive && angle_ > 0) || (~obj.isNegetive && angle_ < 0)
                obj.angle = obj.EnleagleAngle(angle_ + pi);
            else
                obj.angle = obj.EnleagleAngle(angle_);
            end
        end

        %% transform correct angle to k, is_negetive
        function obj = Angle2iN(obj)
            obj.isNegetive = obj.angle < 0;
        end

        %% enleagle the angle to make sure it in [-pi,pi)
        function angle_ = EnleagleAngle(~, ipt_angle_)
            angle_ = mod(ipt_angle_, 2 * pi);

            if angle_ > pi
                angle_ = angle_ - 2 * pi;
            end
        end

        function is_on_ = PointIsOn(obj, point_)
            % FIXME % unsure precision issue
            if point_.x == obj.GetxFromABCy(point_.y)
                if obj.isNegetive
                    if obj.A == 0
                        is_on_ = obj.endpoint.x > point_.x;
                    else
                        is_on_ = obj.endpoint.y > point_.y;
                    end

                else
                    is_on_ = obj.endpoint.y < point_.y;
                end
            end
        end

        function [firstMerge_, firstMerge_index_] = FindFirstMerge(obj, point1_, point2_) %%FIXME%%
            if obj.isNegetive
                if obj.A == 0
                    if point1_.x < point2_.x
                        firstMerge_ = point2_;
                        firstMerge_index_ = 2;
                    else
                        firstMerge_ = point1_;
                        firstMerge_index_ = 1;
                    end
                else
                    if point1_.y < point2_.y
                        firstMerge_ = point2_;
                        firstMerge_index_ = 2;
                    else
                        firstMerge_ = point1_;
                        firstMerge_index_ = 1;
                    end
                end
            else
                if point1_.y > point2_.y
                    firstMerge_ = point2_;
                    firstMerge_index_ = 2;
                else
                    firstMerge_ = point1_;
                    firstMerge_index_ = 1;
                end
            end
        end
    end
end