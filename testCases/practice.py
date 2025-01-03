# String Reversal:
# def rev_str(strng):
#     a = ''
#     for i in strng:
#         a = i+a
#     return a
#
# x = rev_str('1234')
# print(x)



# Printing count of each letter in a  string:
# def dupl_str(s):
#     dict = {}
#     set = ()
#     for i in s:
#         if i in dict:
#             dict[i] = dict[i]+1
#         else:
#             dict[i] = 1
#     return dict
# x = dupl_str("Geeks for geeks")
# print(x)



# Printing unique letters in a string:
# def dupl_str(s):
#     dicti = []
#     seen = set()
#     for i in s:
#         if i not in dicti:
#             dicti.append(i)
#             seen.add(i)
#     return dicti
# x = dupl_str("Geeks for geeks")
# print(x)



dict = {'a' : 1,
	'b' : 2,
	'c' : ['x','y','z',3]}
dict['c'].insert(0,'abc')
print(dict)
# for i in dict.keys():
# 	print(i)