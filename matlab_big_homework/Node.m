classdef Node
    properties
        MAX_OBJECT_COUNT = 5
        Max_Deep = 4;

        LEFT_TOP = 1;
        LEFT_BOTTOM = 2;
        RIGHT_TOP = 3;
        RIGHT_BOTTOM = 4;

        boundary; % Border
        elementSet; % MapArray<Ball>
        childs; % MapArray<Node>

        deep; % int
    end

    methods
        function obj = Node(boundary_, deep_, max_deep_)
            obj.boundary = boundary_;
            obj.deep = deep_;
            obj.Max_Deep = max_deep_;
            obj.elementSet = MapArray();
            obj.childs = MapArray();
        end

        function obj = insert(obj, element_)
            if obj.boundary.isBallImpact(element_)
                return;
            end

            if obj.childs.len() ~= 0
                quadIndex = obj.quadrantOf(element_);
                if quadIndex ~= -1
                    obj.childs.replace(quadIndex, element_);
                    return;
                end
            end

            obj.elementSet = obj.elementSet.append(element_);
            if obj.childs.len() == 0 && ...
                    obj.elementSet.len() > obj.MAX_OBJECT_COUNT && ...
                    obj.deep < obj.Max_Deep
                obj.split();
            end
        end

        function split(obj)
            x_mid = (obj.boundary.x1 + obj.boundary.x2) / 2;
            y_mid = (obj.boundary.y1 + obj.boundary.y2) / 2;

            obj.childs = obj.childs.append(Node(Border( ...
                obj.boundary.x1, ...
                x_mid, ...
                obj.boundary.y1, ...
                y_mid ...
            ), obj.deep + 1, obj.Max_Deep));

            obj.childs = obj.childs.append(Node(Border( ...
                obj.boundary.x1, ...
                x_mid, ...
                y_mid, ...
                obj.boundary.y2 ...
            ), obj.deep + 1, obj.Max_Deep));

            obj.childs = obj.childs.append(Node(Border( ...
                x_mid, ...
                obj.boundary.x2, ...
                obj.boundary.y1, ...
                y_mid ...
            ), obj.deep + 1, obj.Max_Deep));

            obj.childs = obj.childs.append(Node(Border( ...
                x_mid, ...
                obj.boundary.x2, ...
                y_mid, ...
                obj.boundary.y2 ...
            ), obj.deep + 1, obj.Max_Deep));

            elementSetTemp = obj.elementSet;
            obj.elementSet = MapArray();
            for index = 1 : length(elementSetTemp)
                obj.insert(elementSetTemp.get(index));
            end
        end

        function index = quadrantOf(obj, ball_)
            x_mid = (obj.boundary.x1 + obj.boundary.x2) / 2;
            y_mid = (obj.boundary.y1 + obj.boundary.y2) / 2;

            index = -1;
            if ball_.position.x + ball_.radius < x_mid && ball_.position.y - ball_.radius > y_mid
                index = obj.LEFT_TOP;
            elseif ball_.position.x + ball_.radius < x_mid && ball_.position.y + ball_.radius < y_mid
                index = obj.LEFT_BOTTOM;
            elseif ball_.position.x - ball_.radius > x_mid && ball_.position.y - ball_.radius > y_mid
                index = obj.RIGHT_TOP;
            elseif ball_.position.x - ball_.radius > x_mid && ball_.position.y + ball_.radius < y_mid
                index = obj.RIGHT_BOTTOM;
            end
        end

        function check_array_ = retrieve(obj, ball_)
            if obj.childs.len() ~= 0
                index = quadrantOf(ball_);
                if index ~= -1
                    check_array_ = obj.childs.get(index).retrieve(ball_);
                else
                    check_array_ = [];
                    for jndex = 1 : obj.childs.len()
                        inter = obj.childs.get(jndex).boundary.isImpact_(ball_);
                        if inter == true
                            check_array_ = extern_struct_arr(check_array_, obj.childs.get(jndex).retrieve(inter));
                        end
                    end
                end
            else
                check_array_ = obj.elementSet;
            end
        end
    end
end