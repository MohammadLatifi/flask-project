def route_function_wrapper(cls_instance, function_name):
    def route_function():
        function = getattr(cls_instance, function_name)
        return function()
    return route_function