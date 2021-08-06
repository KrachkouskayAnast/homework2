
# print(dir(l))
# ['__add__', 
# '__class__', 
# '__class_getitem__',
#  '__contains__', 
# '__delattr__', '__delitem__',
# '__doc__',
#  '__eq__', 
# '__format__', 
# '__ge__', 
# '__getattribute__',
#  '__getitem__', 
# '__gt__', 
# '__hash__',
#  '__iadd__',
#  '__imul__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__', 
# '__mul__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__', 
# '__repr__', 
# '__reversed__', 
# '__rmul__', 
# '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__', 
# '__subclasshook__',
#  'clear', 
# 'copy',
#  'count', 
#  'index',
#  'insert', 
# 'pop',
#  'remove',
#  'reverse',
#  'sort'
#  l.append добавляет элемент в конец списка
# l.extend(L) добавляет в конец списка все элементы списка L
# l = ['sdsf', 325, [1000, 111], 'jkli', 123] 
# l.append("sdsf")
# l.append(325)
# l.append([])
# l[2].append(1000)
# l[2].append (111)
# # [] квадратные скобки  это новый  лист в листе. 
# l.extend(["jkli",123])
# print(l, l[0],l[1],l[2])
# # l.pop()
# # print(l)
# # удаляет ([]) элемент и возвращает = показывает его в консоль
# # l.reverse()
# # разворачивает список
# count = l.count(325)
# print(count)
# len = len(l)
# print(len)
# x = 325 in l
# y = 'sds' in l
# print(x,y)


# q= ('sde',)
# print(q, type(q))
# q = [0]
# # # tuple не меняеться 
# d = {"Name":"Anastasiya"}
# print (d)
# c= dict(a= 123, b=345, d= 789)
# # get = c.get('e')
# # # возвращает значение value для указанного ключа, если ключа нет none
# # print(get)
# # print("Name:",d.get("Name"))
# keys = c.keys()
# print(keys)
# values = c.values()
# print(values)
# items =  c.items()
# print(items)
# #  возвращает ключи, значения, пары
# #  если работать  (revers) то переводить в list
# l2 = list(keys)
# print (l2)

# s = set([123,34,45])
# # не хранит порядок у него он свой
# print(type(s),s,len(s))
# for x in s:
#     print(x)

# a = 500
# if (a > 5) and (a < 100):
#     print("Bigger")
# else:
#     print("Smoller")

a = 5
# if (a== 1) or (a==3) or (a==4):
#     print("Bigger")
# elif (a==2):
#     print("Big")
# else:
#     print("Smoller")

# if a in (1, 2, 3, 4,):
# # if a in range (1, 5):   не включая 5
#     print("Bigger")
# else:
#      print("Smoller")

# print ("bigger" if a in range(1, 5) else "smoller")

# is_nice = 1 is 1
# print(("not nice", "nice")[is_nice])
# # выводим тьюпл 0 значение false, 1 значение true

sone_none = "None"
print( sone_none or "It is None")



# shop = {
#     "milk" : 2,
#     "butter" : 5,
#     "flover" : 7,
#     }
#     a = input()
#     print(shop.get(a,-1))

# l = [11, 17, 7, 14, 49, 5, 7]
#     for x in l:
#             if x % 7 == 0:
#                 print(x)

