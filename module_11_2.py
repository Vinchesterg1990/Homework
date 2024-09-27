def introspection(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    return info

# Интроспекция числа
number_info = introspection(50)
print(number_info)

# # Интроспекция строки
# string_info = introspection('Привет')
# print(string_info)
#
# # Интроспекция списка
# list_info = introspection(['hello', 45, 5, 8])
# print(list_info)