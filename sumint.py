# def sum_of_intervals(intervals):
#     sum = 0
#     lista = []
#     for(x,y) in intervals:
#         z = y - x
#         sum = sum + z
#         # lista.append(sum)
#     return sum


# def sum_of_intervals(intervals):
#     sum = 0
#     lista = []
#     for(x,y) in range(0,len(intervals)):
#         if(intervals[(x,y)] < intervals[(x+1,y+1)]):
#             z = intervals[y] - intervals[x]
#             sum = sum + z
            
#         else:

#         # lista.append(sum)
#     return sum


def sum_of_intervals(intervals):
    container = set()
    for start, end in intervals:
        for n in range(start, end):
            container.add(n)
    return len(container)

print(sum_of_intervals([(1,3),(1,5)]))
