def snail(snail_map):
    new_array = []
    new_list = []
    new_array.append([x for x in snail_map[0]])
    for i in range(1,len(snail_map)-1):
        new_array.append([snail_map[i][-1]])
    reverse_end = snail_map[len(snail_map)-1]
    reverse_end.reverse()
    new_array.append(reverse_end)
    for i in range(1,len(snail_map)-1):
        array_append = snail_map[i][:len(snail_map[i])-1]
        new_array.append(array_append)

    last_array = [x for sub in new_array for x in sub ]

    new_list = [new_list.append(n) for n in last_array if n not in new_list]

    print(new_list)

    return new_list

snail([[1,2,3],
         [8,9,4],
         [7,6,5]])