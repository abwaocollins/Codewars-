def get_string_lists(a_list):
    new_list = []
    for value in a_list:
        if isinstance(value, str):
            new_list.append(value)
    return new_list
mixed_list = [1, "Jeff", 23.3, "Bruce", "james"]
print(get_string_lists(mixed_list))