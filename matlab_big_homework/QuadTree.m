classdef QuadTree
    properties
        Max_Deep;
        root;
    end

    methods
        function obj = QuadTree(border_, max_deep_)
            obj.Max_Deep = max_deep_;
            obj.root = Node(border_, 0, obj.Max_Deep);
        end

        function obj = insert(obj, ball_)
            obj.root = obj.root.insert(ball_);
        end

        function check_arr = retrieve(obj, ball_)
            check_arr = obj.root.retrieve(ball_);
        end
    end
end