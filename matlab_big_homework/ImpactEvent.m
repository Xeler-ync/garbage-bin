classdef ImpactEvent % I need pointer !!!
    properties
        ball; % index
        impactObject; % index, -1 means border
        msg; % str
    end

    methods
        function obj = ImpactEvent(ball_, impactObject_, msg_)
            obj.ball = ball_;
            obj.impactObject = impactObject_;
            obj.msg = msg_;
        end

        function is_eq_ = eq(obj, ipt_)
            is_eq_ = ((obj.ball == ipt_.ball) && (obj.impactObject == ipt_.impactObject)) || ...
                     ((obj.ball == ipt_.impactObject) && (obj.impactObject == ipt_.ball));
        end
    end
end