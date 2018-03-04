list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
# list1.pop()
print(list1)

def remove_com(data):
    new_list = []
    for i in data:
        if i not in new_list:
            new_list.append(i)
    return new_list


result = remove_com([1,2,1,2,3,4,2,65,7])
print(result)





