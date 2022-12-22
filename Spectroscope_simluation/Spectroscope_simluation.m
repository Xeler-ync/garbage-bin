clear all;
%% init global config
global MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT SPHERICAL_MIRROR_RADIUS HALF_SPHERICAL_ANGLE;
MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT = 100;
SPHERICAL_MIRROR_RADIUS = 101.6 * 2;
SPHERICAL_MIRROR_DIAMETER = 25.4;
HALF_SPHERICAL_ANGLE = asin((SPHERICAL_MIRROR_DIAMETER/2) / SPHERICAL_MIRROR_RADIUS);

%% init global constant
start_point = Point_(0, 0);



mirror_position = [
    Segment( ...
        Point_(9, -0.7474), ...
        Point_(11, 0.7474) ...
    ), ...
    Segment( ...
        Point_(55, 0), ...
        Point_(85, 0) ...
    ), ...
    Segment( ...
        Point_(125, 3.7370), ...
        Point_(135,- 3.7370) ...
    ), ...
    Segment( ...
        Point_(150, 10), ...
        Point_(150, -10) ...
    )
];
mirror_total = length(mirror_position);

circle_1 = CirclePeriod( ...
    Point_(40, -SPHERICAL_MIRROR_RADIUS/2), ...
    SPHERICAL_MIRROR_RADIUS, ...
    Range_(pi/2-HALF_SPHERICAL_ANGLE, pi/2+HALF_SPHERICAL_ANGLE) ...
);

circle_2 = CirclePeriod( ...
    Point_(100, -SPHERICAL_MIRROR_RADIUS/2), ...
    SPHERICAL_MIRROR_RADIUS, ...
    Range_(pi/2-HALF_SPHERICAL_ANGLE, pi/2+HALF_SPHERICAL_ANGLE) ...
);

a = Range_(0, pi*2);

% draw mirror
for i = 1:mirror_total
    plot([mirror_position(i).endpoint1.x, mirror_position(i).endpoint2.x], [mirror_position(i).endpoint1.y, mirror_position(i).endpoint2.y], 'LineWidth', 2);
    hold on;
end
draw_circlePeriod(circle_1);
draw_circlePeriod(circle_2);
%     circle_angle_range_2 ...

% plot([-10000,10000], [0,0], 'LineWidth', 2);
% hold on;
daspect([1,1,1])

%% get random point
light_total_ = 100;
point_array_= mirror_position(1).endpoint1.x : 0.0001 : mirror_position(1).endpoint2.x;

%% draw light
for i = 1 : light_total_
    % random point on circle1
    random_x = point_array_(randperm(numel(point_array_), 1));
    merge_1 = Point_( ...
        random_x, mirror_position(1).GetyFromABCx(random_x) ...
    );

    plot([start_point.x, merge_1.x], [start_point.y, merge_1.y], 'Linewidth', 1);
    hold on;

    incidentRay_ = Ray(NaN, NaN, NaN, Point_(NaN, NaN), false);
    incidentRay_ = incidentRay_.ReflashByTwoPoint(start_point, merge_1);
    incidentRay_.isNegetive = false;
    incidentRay_ = incidentRay_.iN2Angle();

    tgt_line_mirror_ = mirror_position(1);

    [reflectedRay_, is_merged_] = reflect_line_to_circlePeriod_( ...
        tgt_line_mirror_, incidentRay_, circle_1 ...
    );

    if ~is_merged_
        continue;
    end

    tgt_line_mirror_ = mirror_position(2);

    [reflectedRay_, is_merged_] = relfect_circle_( ...
        circle_1, reflectedRay_, tgt_line_mirror_ ...
    );

    if ~is_merged_
        continue;
    end

    [reflectedRay_, is_merged_] = reflect_line_to_circlePeriod_( ...
        tgt_line_mirror_, reflectedRay_, circle_2 ...
    );

    if ~is_merged_
        continue;
    end

    tgt_line_mirror_ = mirror_position(3);

    [reflectedRay_, is_merged_] = relfect_circle_( ...
        circle_2, reflectedRay_, tgt_line_mirror_ ...
    );

    if ~is_merged_
        continue;
    end

    [reflectedRay_, is_merged_] = reflect_( ...
        tgt_line_mirror_, reflectedRay_, mirror_position(4) ...
    );

end













daspect([1,1,1])

%% """ _reflect_line_to_circle_arc
%
% targetLine_   Line
% incidentRay_  Ray
% circlePeriod_ CirclePeriod
%
% return
% reflectedRay_ Ray
% reflected_is_negetive_
% """

function [reflectedRay_, is_merged_] = reflect_line_to_circlePeriod_( ...
    targetLine_, incidentRay_, circlePeriod_ ...
)
    [reflectedRay_] = calc_reflect_light_(targetLine_, incidentRay_);
    [mergePoint_, is_merged_] = get_line_merge_arc(reflectedRay_, circlePeriod_);
    mergeMirror_ = get_cross_point(targetLine_, incidentRay_);

    if is_merged_
        plot([mergeMirror_.x, mergePoint_.x], [mergeMirror_.y, mergePoint_.y], 'Linewidth', 1);
        hold on;
    else
        % let delta has same direction with light
        if reflectedRay_.isNegetive
            force_y_symbol_ = -1;
        else
            force_y_symbol_ = 1;
        end

        A_B_is_opposite_ = (reflectedRay_.A >= 0) ~= (reflectedRay_.B >= 0);

        global MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT;
        merge_tgt_x_extended_ = mergeMirror_.x + MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT * abs(reflectedRay_.B)/sqrt(reflectedRay_.A^2+reflectedRay_.B^2) * force_y_symbol_ * ~A_B_is_opposite_;
        merge_tgt_y_extended_ = mergeMirror_.y + MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT * abs(reflectedRay_.A)/sqrt(reflectedRay_.A^2+reflectedRay_.B^2) * force_y_symbol_;

        % plot([mergeMirror_.x, merge_tgt_x_extended_], [mergeMirror_.y, merge_tgt_y_extended_], 'Linewidth', 1);
        hold on;
    end

end

%% get distance of two point
function distance_ = get_distance_from_two_point( ...
    point1, point2 ...
)
    distance_ = sqrt((point1.x1_-point2.x2_)^2+(point1.y1_-point2.y2_)^2);
end

%% get merge of line to arc
function [mergePoint_, is_merged_] = get_line_merge_arc( ...
    line_, circle_ ...
)
    [merge_1_, merge_2_, is_merged_] = get_ray_merge_circle( ...
        line_, circle_ ...
    );
    if ~is_merged_
        % shut the fucking compiler up
        mergePoint_ = Point_(0, 0);

        return;
    end


    merge_1_on_arc = point_is_on_circlePeriod( ...
        merge_1_, circle_ ...
    );
    merge_2_on_arc = point_is_on_circlePeriod( ...
        merge_2_, circle_ ...
    );

    if ~merge_1_on_arc && merge_2_on_arc
        mergePoint_ = merge_2_;
    elseif merge_1_on_arc && ~merge_2_on_arc
        mergePoint_ = merge_1_;
    elseif merge_1_on_arc && merge_2_on_arc
        if line_.isNegetive
            if line_A_ == 0
                if merge_X1_ < merge_X2_
                    mergePoint_ = merge_2_;
                else
                    mergePoint_ = merge_1_;
                end
            else
                if merge_1_.y < merge_2_.y
                    mergePoint_ = merge_2_;
                else
                    mergePoint_ = merge_1_;
                end
            end
        else
            if merge_1_.y > merge_2_.y
                mergePoint_ = merge_2_;
            else
                mergePoint_ = merge_1_;
            end
        end
    else
        is_merged_ = false;
        % shut the fucking compiler up
        mergePoint_ = Point_(0, 0);

        return;
    end

end

%% """_reflect_circle
%
% circle_ Circle
% tgtSegment_   Segment
% incidentRay_  Ray
%
% return
% reflectedRay_ Ray
% reflected_is_negetive_
% """

function [reflectedRay_, is_merged_] = relfect_circle_( ...
    circle_, incidentRay_, tgtSegment_ ...
)
    [mergePoint_, is_merged_] = get_line_merge_arc( ...
        incidentRay_, circle_ ...
    );
    if ~is_merged_
        % shut the fucking compiler up
        reflectedRay_ = Ray(NaN, NaN, NaN, true, Point_(NaN, NaN));

        return;
    end
    lineMergeToCenter_ = Line(NaN, NaN, NaN);
    lineMergeToCenter_ = lineMergeToCenter_.ReflashByTwoPoint(circle_.center, mergePoint_);

    % new a fake mirror for reflection
    fakeMirror_ = Segment(Point_(NaN, NaN), Point_(NaN, NaN));
    fakeMirror_.A = -lineMergeToCenter_.B;
    fakeMirror_.B = lineMergeToCenter_.A;
    fakeMirror_.C = - (fakeMirror_.A*mergePoint_.x + fakeMirror_.B*mergePoint_.y);

    if abs(incidentRay_.A/incidentRay_.B) < 1
        fakeMirror_ = fakeMirror_.ReflashByTwoPoint( ...
            Point_(mergePoint_.x - 1145141919810, fakeMirror_.GetyFromABCx(mergePoint_.x - 1145141919810)), ...
            Point_(mergePoint_.x + 1145141919810, fakeMirror_.GetyFromABCx(mergePoint_.x + 1145141919810)) ...
        );
    else
        fakeMirror_ = fakeMirror_.ReflashByTwoPoint( ...
            Point_(fakeMirror_.GetxFromABCy(mergePoint_.y - 1145141919810), mergePoint_.y - 1145141919810), ...
            Point_(fakeMirror_.GetxFromABCy(mergePoint_.y + 1145141919810), mergePoint_.y + 1145141919810) ...
        );
    end

    [reflectedRay_, is_merged_] = reflect_( ...
        fakeMirror_, incidentRay_, tgtSegment_ ...
    );
end

%% check line is merge to circle
function is_merged_ = line_is_merge_circle_segment_( ...
    line_, circlePeriod_ ...
)
    if distance_point_line(circlePeriod_ ,line_) > circlePeriod_.radius
        is_merged_ = false;
        return;
    end

    [merge_x1_,merge_x1_,merge_x2_,merge_y2_] = get_ray_merge_circle( ...
        line_A_,line_B_,line_C_, line_is_negetive_, ...
        circle_center_, circle_radius_, circle_angle_ ...
    );

end

%% check point on circular arc
function is_on = point_is_on_circlePeriod( ...
    point_, circlePeriod_ ...
)
    arcMiddle_ = Point_( ...
        circlePeriod_.center.x + circlePeriod_.radius * cos((circlePeriod_.range.lower+circlePeriod_.range.upper)/2), ...
        circlePeriod_.center.y + circlePeriod_.radius * sin((circlePeriod_.range.lower+circlePeriod_.range.upper)/2) ...
    );

    if point_.x == arcMiddle_.x && point_.y == arcMiddle_.y
        is_on = true;
        return;
    end

    endPoint1_ = Point_( ...
        circlePeriod_.center.x+circlePeriod_.radius*cos(circlePeriod_.range.lower), ...
        circlePeriod_.center.y+circlePeriod_.radius*sin(circlePeriod_.range.lower) ...
    );
    endPoint2_ = Point_( ...
        circlePeriod_.center.x+circlePeriod_.radius*cos(circlePeriod_.range.upper), ...
        circlePeriod_.center.y+circlePeriod_.radius*sin(circlePeriod_.range.upper) ...
    );

    segmentPointCenter_ = Segment( ...
        point_, circlePeriod_.center ...
    );
    segmentEndpointCenterLower_ = Segment( ...
        endPoint1_, arcMiddle_...
    );
    segmentEndpointCenterUpper_ = Segment( ...
        endPoint2_, arcMiddle_...
    );

    is_on = line_segment_is_merge_line_segment_( ...
        segmentPointCenter_, segmentEndpointCenterLower_ ...
    ) || line_segment_is_merge_line_segment_( ...
        segmentPointCenter_, segmentEndpointCenterUpper_ ...
    );
end

%% get the order in which the ray merge the circle, must has 2
function [point1_, point2_, is_merged_] = get_ray_merge_circle( ...
    ray_, circle_ ...
)
    center_to_line_ = distance_point_line(circle_.center, ray_);

    is_merged_ = center_to_line_ <= circle_.radius;
    if ~is_merged_
        % shut the fucking compiler up
        point1_ = Point_(NaN, NaN);
        point2_ = Point_(NaN, NaN);

        return;
    end

    lineCenterToShortestDistancePoint_ = Line( ...
        -ray_.B, ray_.A, ...
        - (-ray_.B*circle_.center.x + ray_.A*circle_.center.y) ...
    );

    shortestDistancePoint_ = get_cross_point( ...
        lineCenterToShortestDistancePoint_, ray_ ...
    );
    shortest_distance_point_to_merge_point_ = sqrt(circle_.radius*circle_.radius - center_to_line_*center_to_line_);

    if ray_.B == 0
        if ray_.isNegetive
            point1_ = Point(shortestDistancePoint_.x, shortestDistancePoint_.y + shortest_distance_point_to_merge_point_);
            point2_ = Point(shortestDistancePoint_.x, shortestDistancePoint_.y - shortest_distance_point_to_merge_point_);
        else
            point1_ = Point(shortestDistancePoint_.x, shortestDistancePoint_.y - shortest_distance_point_to_merge_point_);
            point2_ = Point(shortestDistancePoint_.x, shortestDistancePoint_.y + shortest_distance_point_to_merge_point_);
        end
    elseif ray_.A == 0
        if ray_.isNegetive
            point1_ = Point(shortestDistancePoint_.x + shortest_distance_point_to_merge_point_, shortestDistancePoint_.y);
            point2_ = Point(shortestDistancePoint_.x - shortest_distance_point_to_merge_point_, shortestDistancePoint_.y);
        else
            point1_ = Point(shortestDistancePoint_.x - shortest_distance_point_to_merge_point_, shortestDistancePoint_.y);
            point2_ = Point(shortestDistancePoint_.x + shortest_distance_point_to_merge_point_, shortestDistancePoint_.y);
        end
    else
        if ray_.isNegetive
            y1_ = shortestDistancePoint_.y + sin(ray_.angle) * shortest_distance_point_to_merge_point_;
            y2_ = shortestDistancePoint_.y - sin(ray_.angle) * shortest_distance_point_to_merge_point_;
        else
            y1_ = shortestDistancePoint_.y - sin(ray_.angle) * shortest_distance_point_to_merge_point_;
            y2_ = shortestDistancePoint_.y + sin(ray_.angle) * shortest_distance_point_to_merge_point_;
        end
        point1_ = Point_(ray_.GetxFromABCy(y1_), y1_);
        point2_ = Point_(ray_.GetxFromABCy(y2_), y2_);
    end
end

%% get distance of point to line
function distance_ = distance_point_line(point_ ,line_)
    distance_ = abs(line_.A*point_.x + line_.B*point_.y + line_.C) / sqrt(line_.A*line_.A+line_.B*line_.B);
end

%% get x from ABCy
function x_ = get_x_from_ABCy(line_, y_)
    x_ = (-line_.C - line_.B*y_) / line_.A;
end

%% get y from ABCx
function y_ = get_y_from_ABCx(line_, x_)
    y_ = (-line_.C - line_.A*x_) / line_.B;
end

%% """ _draw_circle
%
% center_      struct('x',float,'y',float)
% radius_      length
% angle_       struct('lower',float,'upper',float)
% """
function draw_circlePeriod(circlePeriod_)
    plot_period_ = circlePeriod_.range.lower : 0.0001 : circlePeriod_.range.upper;
    x_array_ = circlePeriod_.center.x + circlePeriod_.radius * cos(plot_period_);
    y_array_ = circlePeriod_.center.y + circlePeriod_.radius * sin(plot_period_);

    plot(x_array_,y_array_);
    hold on;
end

%% """_reflect
%
% mirror_Ax_    point
% mirror_Ay_
% mirror_Bx_
% mirror_By_
% incident_A_   Ax + By + C = 0
% incident_B_
% incident_C_
% incident_is_negetive_
% tgt_Ax_   Ax + By + C = 0
% tgt_Ay_
% tgt_Bx_
% tgt_By_
%
% return
% reflected_A_  Ax + By + C = 0
% reflected_B_
% reflected_C_
% reflected_is_negetive_
% """
function [reflectedRay_, is_merged_] = reflect_( ...
    mirror_, incidentRay_, tgtSegment_ ...
)
    % incident

    reflectedRay_ = calc_reflect_light_( ...
        mirror_, incidentRay_ ...
    );

    mergeMirror_ = get_cross_point(mirror_, incidentRay_);
    mergeTgt_ = get_cross_point(reflectedRay_, tgtSegment_);

    % check mergable of reflected and target and draw it if merge
    is_merged_ = line_is_merge_line_segment_( ...
        reflectedRay_, tgtSegment_ ...
    );
    if is_merged_
        plot([mergeMirror_.x, mergeTgt_.x], [mergeMirror_.y, mergeTgt_.y], 'Linewidth', 1);
        hold on;
    else
        % let delta has same direction with light
        if reflectedRay_.isNegetive
            force_y_symbol_ = -1;
        else
            force_y_symbol_ = 1;
        end

        A_B_is_opposite_ = (reflectedRay_.A >= 0) ~= (reflectedRay_.B >= 0);

        global MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT;
        merge_tgt_X_extended_ = mergeMirror_.x + MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT * abs(reflectedRay_.B)/sqrt(reflectedRay_.A^2+reflectedRay_.B^2) * force_y_symbol_ * ~A_B_is_opposite_;
        merge_tgt_Y_extended_ = mergeMirror_.y + MAX_UNMERGE_REFLECTION_PRESENT_LINE_LENGHT * abs(reflectedRay_.A)/sqrt(reflectedRay_.A^2+reflectedRay_.B^2) * force_y_symbol_;

        % plot([mergeMirror_.x, merge_tgt_X_extended_], [mergeMirror_.y, merge_tgt_Y_extended_], 'Linewidth', 1);
        hold on;
    end

end


%% get merge point from Standerd-pointForm
function point_ = get_cross_point(line1_, line2_)
    point_ = Point_( ...
        ((-line1_.C) * line2_.B - line1_.B * (-line2_.C)) / (line1_.A * line2_.B - line1_.B * line2_.A), ...
        (line1_.A * (-line2_.C) - (-line1_.C) * line2_.A) / (line1_.A * line2_.B - line1_.B * line2_.A) ...
    );
end

%% check line is merge to line segment
function is_merged_ = line_is_merge_line_segment_( ...
    line_, segment_ ...
    )
    merge_tgt_ = line_.GetCrossPoint(segment_);
    is_merged_ = ...
        (segment_.B ~= 0 && ~(merge_tgt_.x <= min(segment_.endpoint1.x, segment_.endpoint2.x)) && ~(merge_tgt_.x >= max(segment_.endpoint1.x, segment_.endpoint2.x))) ...
        || (segment_.B == 0 && ~(merge_tgt_.y <= min(segment_.endpoint1.y, segment_.endpoint2.y)) && ~(merge_tgt_.y >= max(segment_.endpoint1.y, segment_.endpoint2.y)));
end

%% check line segment is merge to line segment
function is_merged_ = line_segment_is_merge_line_segment_( ...
    segment1_, segment2_ ...
    )

    merge_tgt_ = segment1_.GetCrossPoint(segment2_);
    is_merged_ = ...
        ((segment1_.B ~= 0 && ~(merge_tgt_.x < min(segment1_.endpoint1.x, segment1_.endpoint2.x)) && ~(merge_tgt_.x > max(segment1_.endpoint1.x, segment1_.endpoint2.x))) ...
        || (segment1_.B == 0 && ~(merge_tgt_.y < min(segment1_.endpoint1.y, segment1_.endpoint2.y)) && ~(merge_tgt_.y > max(segment1_.endpoint1.y, segment1_.endpoint2.y)))) ...
        && ((segment2_.B ~= 0 && ~(merge_tgt_.x < min(segment2_.endpoint1.x, segment2_.endpoint2.x)) && ~(merge_tgt_.x > max(segment2_.endpoint1.x, segment2_.endpoint2.x))) ...
        || (segment2_.B == 0 && ~(merge_tgt_.y < min(segment2_.endpoint1.y, segment2_.endpoint2.y)) && ~(merge_tgt_.y > max(segment2_.endpoint1.y, segment2_.endpoint2.y))));
end

%% enleagle the angle to make sure it in [-pi,pi)
function angle_ = enleagle_angle_(ipt_angle_)
    angle_ = mod(ipt_angle_, 2 * pi);

    if angle_ > pi
        angle_ = angle_ - 2 * pi;
    end

end

%% make sure normal is forward to incident
function normal_angle_ = get_suitable_normal_angle(normal_k_, incident_angle_)
    normal_angle_ = enleagle_angle_(atan(normal_k_));

    if abs(normal_angle_ - incident_angle_) < pi / 2
        normal_angle_ = enleagle_angle_(normal_angle_ + pi);
    end

end

%% Two-pointForm to Standerd-pointForm
function line_ = Tow_point_to_Standerd_func_(point1_, point2_)
    line_ = Line( ...
        point2_.y - point1_.y, ...
        point1_.x - point2_.x, ...
        point2_.x * point1_.y - point1_.x * point2_.y ...
    );
end

%% Standerd-pointForm to kb-pointForm
function [k_, b_] = Standerd_to_kb_func(line_)
    k_ = -line_.A / line_.B;
    b_ = -line_.C / line_.B;
end

%% kb-pointForm to Standerd-pointForm
function line_ = kb_to_Standerd_func(k_, b_)
    line_ = Line(k_, -1, b_);
end

%% transform k, is_negetive to correct angle with correct direction
function angle_ = k_in_to_a(k_, is_negetive_)
    angle_ = atan(k_);

    if is_negetive_ && angle_ > 0 || ~is_negetive_ && angle_ < 0
        angle_ = enleagle_angle_(angle_ + pi);
    end

end

%% transform correct angle to k, is_negetive
function [k_, is_negetive_] = a_to_k_in(angle_)
    k_ = tan(angle_);
    is_negetive_ = angle_ < 0;
end

%% """_calc_reflect_light
%
% mirrorLine_   Line
% incidentRay_  Ray
%
% return
% reflectedRay_ Ray
% """

function [reflectedRay_] = calc_reflect_light_(mirrorLine_, incidentRay_)

    if mirrorLine_.A * incidentRay_.B == mirrorLine_.B * incidentRay_.A
        reflectedRay_ = Ray( ...
            incidentRay_.A, ...
            -incidentRay_.B, ...
            incidentRay_.C, ...
            ~incidentRay_.isNegetive, ...
            mirrorLine_.GetCrossPoint(incidentRay_) ...
        );

    elseif incidentRay_.B == 0
        reflectedRay_ = Ray( ...
            NaN, ...
            NaN, ...
            NaN, ...
            true, ...
            Point_( ...
            -incidentRay_.C / incidentRay_.A, ...
            (-mirrorLine_.A + (-mirrorLine_.A * -incidentRay_.C / incidentRay_.A)) / mirrorLine_.B ...
        ) ...
        );

        reflected_k_ =- (-incidentRay_.A / incidentRay_.B);
        reflectedRay_ = reflectedRay_.ReflashBykb( ...
            reflected_k_, ...
            reflectedRay_.endpoint.y - reflected_k_ * reflectedRay_.endpoint.x ...
        );
        [mirrorLine_k_, ~] = Standerd_to_kb_func(mirrorLine_);

        if abs(mirrorLine_k_) > 1
            reflectedRay_.isNegetive = incidentRay_.isNegetive;
        else
            reflectedRay_.isNegetive = ~incidentRay_.isNegetive;
        end

    elseif mirrorLine_.B == 0
        merge_x_ = mirrorLine_.C / mirrorLine_.A;
        merge_y_ = incidentRay_.GetyFromABCx(merge_x_);

        reflected_k_ =- (-incidentRay_.A / incidentRay_.B);

        reflectedRay_ = Ray( ...
            reflected_k_, ...
            -1, ...
            merge_y_ - reflected_k_ * merge_x_, ...
            incidentRay_.isNegetive, ...
            Point_( ...
            merge_x_, ...
            merge_y_ ...
        ) ...
        );

    elseif mirrorLine_.A == 0
        merge_y_ = -mirrorLine_.C / mirrorLine_.B;
        merge_x_ = incidentRay_.GetxFromABCy(merge_y_);

        reflected_k_ =- (-incidentRay_.A / incidentRay_.B);

        reflectedRay_ = Ray( ...
            reflected_k_, ...
            -1, ...
            merge_y_ - reflected_k_ * merge_x_, ...
            ~incidentRay_.isNegetive, ...
            Point_( ...
                merge_x_, ...
                merge_y_ ...
            ) ...
        );
    else
        normal_k_ = -1 / (-mirrorLine_.A / mirrorLine_.B);
        normal_angle_ = enleagle_angle_( ...
            get_suitable_normal_angle(normal_k_, incidentRay_.angle) ...
        );

        merge_ = mirrorLine_.GetCrossPoint(incidentRay_);

        reflected_angle_ = enleagle_angle_(normal_angle_ + normal_angle_ - incidentRay_.angle + pi);

        % pre calc result
        [reflected_k_, reflected_is_negetive_] = a_to_k_in(reflected_angle_);

        reflectedRay_ = Ray( ...
            reflected_k_, ...
            -1, ...
            merge_.y - reflected_k_ * merge_.x, ...
            reflected_is_negetive_, ...
            merge_ ...
        );

        % make sure light on the same site of mirror
        checkPointReflected = Point_(NaN, NaN);

        if reflected_angle_ >= 0
            checkPointReflected.y = merge_.y + 5;
        else
            checkPointReflected.y = merge_.y - 5;
        end

        checkPointReflected.x = reflectedRay_.GetxFromABCy(checkPointReflected.y);

        checkPointIncident = Point_(NaN, NaN);

        if ~incidentRay_.isNegetive
            checkPointIncident.y = merge_.y - 5;
        else
            checkPointIncident.y = merge_.y + 5;
        end

        checkPointIncident.x = incidentRay_.GetxFromABCy(checkPointIncident.y);

        checkSegment_ = Segment(checkPointReflected, checkPointIncident);

        if line_is_merge_line_segment_(mirrorLine_, checkSegment_)
            reflectedRay_.isNegetive = ~reflectedRay_.isNegetive;
        end

    end

end
