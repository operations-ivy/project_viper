x = lambda x: x+1
print(x(2))

new_list = [{'name': 'abe', 'count': 2},
            {'name': 'tim', 'count': 8},
            {'name': 'bil', 'count': 1}]

list_of_lists = [[3,7],
                 [9,10],
                 [3,1],
                 [2,2]]

new_list.sort(key=lambda x: x['count'], reverse=True)
list_of_lists.sort(key=lambda x: x[1], reverse=True)

print(new_list)
print(list_of_lists)


def modify_mod(num):
    return num%100

plain_list = [155, 371, 219, 640, 263]

# plain_list.sort(key=modify_mod)

plain_list.sort(key=lambda x: x%100)

print(plain_list)

def modify_split(split_string):
    return split_string.split()[1]

name_list = ['good bad', 'plain fancy', 'cold hot']

# name_list.sort(key=modify_split, reverse=True)

name_list.sort(key=lambda x: x.split()[1], reverse=True)

print(name_list)
