from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# count2 = countries[:-1]

# def european(x,y):
#     return f"{x}, {y}"

# print(reduce(european,count2),f"and {countries[-1]} are North European countries")
print(reduce(lambda x,y : f"{x}, {y}",countries[:-1]),f"and {countries[-1]} are North European countries")

