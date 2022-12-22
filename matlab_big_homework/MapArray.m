classdef MapArray
    % Inserting a custom class into array initialized with [] will report an error, replace array with this class
    % array在使用[]初始化后，插入自定义类会报错，所以使用这个类替换
    properties
        content; % containers.Map private
        key; % Array<string> private
    end

    methods
        function obj = MapArray()
            obj.content = containers.Map;
            obj.key = {};
        end

        function obj = append(obj, ipt_)
            key_name = string(strrep(tempname('\'), '\', '')); % as uuid
            obj.key(obj.len()+1) = {key_name};
            obj.content(key_name) = ipt_;
        end

        function obj = pop(obj, index_)
            remove(obj.content, string(obj.key(index_)));
            obj.key(index_) = [];
        end

        function obj = replace(obj, index_, element_)
            obj.content(string(obj.key(index_))) = element_;
        end

        function ele_ = get(obj, index_)
            ele_ = obj.content(string(obj.key(index_)));
        end

        function len_ = len(obj)
            len_ = length(obj.key);
        end

        function obj = externMapArray(obj, mapArray_)
            for index = 1 : mapArray_.len()
                obj = obj.append(index, mapArray_.get(index));
            end
        end

        function obj = enUnique(obj)
            find_upper = obj.len();
            pop_arr = zeros(1, find_upper);
            for index = 1 : (find_upper-1)
                for jndex = (index+1) : find_upper
                    if obj.get(index) == obj.get(jndex)
                        pop_arr(jndex) = 1;
                    end
                end
            end
            for index = (find_upper) : -1 : 1
                if pop_arr(index) == 1
                    obj = obj.pop(index);
                end
            end
        end
    end
end