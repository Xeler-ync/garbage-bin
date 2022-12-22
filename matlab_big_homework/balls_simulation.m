clear;
%% init
MAIN_BORDER = Border(0, 100, 0, 100);
Ball_Array = [
    Ball( ...
        Speed(-100, 10), ...
        Point_(90, 50), ...
        3, ...
        6 ...
    ), ...
    Ball( ...
        Speed(0, -10), ...
        Point_(50, 90), ...
        2, ...
        4 ...
    ), ...
    Ball( ...
        Speed(20, 50), ...
        Point_(20, 90), ...
        2, ...
        4 ...
    ), ...
    Ball( ...
        Speed(0, 10), ...
        Point_(50, 10), ...
        6, ...
        7 ...
    ) ...
];
TICK_LENGTH = 0.01;
SIMLUATION_LENGHT = 60;
ZERO_TO_PI = 0 : pi/100 : 2*pi;

Min_Radius = Inf;
Max_Radius = -Inf;
Ball_Path_Array = zeros(length(Ball_Array), SIMLUATION_LENGHT/TICK_LENGTH);
for index = 1 : length(Ball_Array)
    Min_Radius = min(Min_Radius, Ball_Array(index).radius);
    Max_Radius = max(Max_Radius, Ball_Array(index).radius);
end
MAX_SPEED = Min_Radius / TICK_LENGTH * 1111111111;
Quadtree_Minimum_Side_Length = 2 / 3 * Max_Radius;
Quadtree_Maximum_Iterations = fix(min(abs(MAIN_BORDER.x1 - MAIN_BORDER.x2), abs(MAIN_BORDER.y1 - MAIN_BORDER.y2)) / Quadtree_Minimum_Side_Length);

%% simluation start
for t = 1 : SIMLUATION_LENGHT / TICK_LENGTH
    quarTree = QuadTree(MAIN_BORDER, Quadtree_Maximum_Iterations);
    time = t * TICK_LENGTH;
    for ball_index = 1 : length(Ball_Array)
        Ball_Array(ball_index) = Ball_Array(ball_index).moveTimePeriod(TICK_LENGTH);
        %% Force calculation %%
        current_fx = -(Ball_Array(ball_index).position.x-abs(MAIN_BORDER.x1 - MAIN_BORDER.x2)/2) / Ball_Array(ball_index).mass;
        current_fy = -(Ball_Array(ball_index).position.y-abs(MAIN_BORDER.y1 - MAIN_BORDER.y2)/2) / Ball_Array(ball_index).mass;
%         current_fx = 0;
%         current_fy = -9.81 * Ball_Array(ball_index).mass;
        Ball_Array(ball_index).speed = Ball_Array(ball_index).speed.increaseSpeed(TICK_LENGTH * current_fx / Ball_Array(ball_index).mass, TICK_LENGTH * current_fy / Ball_Array(ball_index).mass);
        quarTree = quarTree.insert(Ball_Array(ball_index));
    end

    borderImpactCheckMapArray = MapArray();
    ballImpactCheckMapArray = MapArray();
    for ball_index = 1 : length(Ball_Array)
        direction = MAIN_BORDER.ballImpactDirection(Ball_Array(ball_index));
        if direction ~= ""
            borderImpactCheckMapArray = borderImpactCheckMapArray.append(ImpactEvent(ball_index, -1, direction));
        end
        mayImpactMapArray = quarTree.retrieve(Ball_Array(ball_index));
        for may_impact_index = 1 : mayImpactMapArray.len()
            if Ball_Array(ball_index).isBallImpact(mayImpactMapArray.get(may_impact_index))
                tgt_ball_index = -1;
                for ball_index_1 = 1 : length(Ball_Array)
                    if Ball_Array(ball_index_1) == mayImpactMapArray.get(may_impact_index)
                        tgt_ball_index = ball_index_1;
                        break;
                    end
                end
                if ball_index ~= tgt_ball_index
                    ballImpactCheckMapArray = ballImpactCheckMapArray.append(ImpactEvent(ball_index, tgt_ball_index, "BALL"));
                end
            end
        end
    end
    ballImpactCheckMapArray = ballImpactCheckMapArray.enUnique();

    for impact_index = 1 : ballImpactCheckMapArray.len()
        [Ball_Array(ballImpactCheckMapArray.get(impact_index).ball), Ball_Array(ballImpactCheckMapArray.get(impact_index).impactObject)] = Ball_Array(ballImpactCheckMapArray.get(impact_index).ball).impactBall(Ball_Array(ballImpactCheckMapArray.get(impact_index).impactObject));
    end
    for impact_index = 1 : borderImpactCheckMapArray.len()
        Ball_Array(borderImpactCheckMapArray.get(impact_index).ball) = MAIN_BORDER.impactBall(Ball_Array(borderImpactCheckMapArray.get(impact_index).ball), borderImpactCheckMapArray.get(impact_index).msg);
    end

    hold off;
    for ball_index = 1 : length(Ball_Array)
        Ball_Array(ball_index) = Ball_Array(ball_index).speedEnthreshold(MAX_SPEED);
        fill(Ball_Array(ball_index).position.x + Ball_Array(ball_index).radius * cos(ZERO_TO_PI), Ball_Array(ball_index).position.y + Ball_Array(ball_index).radius * sin(ZERO_TO_PI), 'r');
        hold on;
    end
    axis equal
    axis([min(MAIN_BORDER.x1, MAIN_BORDER.x2) max(MAIN_BORDER.x1, MAIN_BORDER.x2) min(MAIN_BORDER.y1, MAIN_BORDER.y2) max(MAIN_BORDER.y1, MAIN_BORDER.y2)])
    M(t) = getframe;
end

movie(M,1,100)
