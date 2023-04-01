# Group elements in a list by their index
my_list = ['a', 'b', 'c', 'd', 'e']
grouped_list = [[] for i in range(len(my_list))]
for i, elem in enumerate(my_list):
    grouped_list[i].append(elem)
print(grouped_list)