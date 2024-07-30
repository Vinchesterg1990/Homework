def apply_all_func(int_list, *functions):
    results = {}
    for functions in functions:
        results[functions.__name__] = functions(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

