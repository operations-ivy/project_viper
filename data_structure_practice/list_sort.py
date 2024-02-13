list1 = [1,2,4]
list2 = [1,3,4]

def merge_two_lists(list1,list2):
    sorted_list = list1 + list2
    sorted_list.sort()

    return sorted_list

print(merge_two_lists(list1,list2))