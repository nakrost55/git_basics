def dict_union(dict1, dict2):    #union of dictionaries
    return {**dict1, **dict2}

def dict_intersection(dict1, dict2):    #intersection of dictionaries
    return {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}

def dict_difference(dict1, dict2):    #difference of diktionaries
    return {k: dict1[k] for k in dict1 if k not in dict2}

def dict_symmetric_difference(dict1, dict2):	#disjunctive sum of dictionaries
    return {**{k: dict1[k] for k in dict1 if k not in dict2},
            **{k: dict2[k] for k in dict2 if k not in dict1}}

def dict_subset(dict1, dict2):	  #inclusion check
    return all(k in dict2 and dict1[k] == dict2[k] for k in dict1)
    
def dict_equality(dict1, dict2):	#equality check
    return dict1 == dict2

def sort_dict(dict_obj, reverse=False):		#function for sorting dictionaries
    return {k: v for k, v in sorted(dict_obj.items(), key=lambda item: item[1], reverse=reverse)}

def flip_dict(dict_obj):	#function for flipping dictionaries
    flipped = {}
    for key, value in dict_obj.items():
        if value in flipped:
            raise ValueError(f"Cannot flip dictionary: multiple keys have the same value ({value})")
        flipped[value] = key
    return flipped

