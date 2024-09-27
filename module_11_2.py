def introspection(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    return info

# Интроспекция числа
number_info = introspection(42)
print(number_info)

# # Интроспекция строки
# string_info = introspection('Hello, World!')
# print(string_info)
#
# # Интроспекция списка
# list_info = introspection(['1', 2, 3, 4.0])
# print(list_info)