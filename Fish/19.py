# 有问题
# def check(str):
#     lenght = len(str)
#     for each in range(lenght):
#         if str[each] != str[-each-1]:
#             print('%s-->不是回文联'%str)
#
# # str = input('请输入对联：')
# # check(str)
# # check(str = '上海自来水来自海上')
# check(str = '你是不是你啊')
#

#
# def check(string):
#     list1 = list(string)
#     list2 = reversed(list1)
#     if list1 == list(list2):
#         return 'shi'
#     else:
#         return 'bushi'
#
# string = input('请输入对联：')
# print(check(string))
# print(check('你是不是你啊'))



def count(*parameter):
    lenght = len(parameter)
    for i in range(lenght):
        letter = 0
        space = 0
        digit = 0
        other = 0
        for each in parameter[i]:
            if each.isspace():
                space += 1
            if each.isdigit():
                digit += 1
            if each.isalpha():
                letter += 1
            else:
                other += 1
    return (space, letter,digit,other)

print(count('i5love you! '))

# help(str)