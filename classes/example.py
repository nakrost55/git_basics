#!/usr/bin/env python3

 task_5 example

def dict_union(dict1, dict2):
    result_dict = dict1.copy()  # копіюємо словник dict1
    result_dict.update(dict2)  # додаємо пари ключ-значення з dict2
    return result_dict

# Приклад 1 використання функції
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

result = dict_union(dict1, dict2)
print(result)”


# Приклад 2
def sort_dict_by_value(d):
    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get)
    for k in sorted_keys:
        sorted_dict[k] = d[k]
    return sorted_dict

dict1 = {"a": 3, "b": 1, "c": 2}
sorted_dict = sort_dict_by_value(dict1)
print(sorted_dict) # {'b': 1, 'c': 2, 'a': 3}
