# class Table:
#     def__init__(self,w,h,l):
#         self.length = l
#             self.width = w
#             self.height = h
#    
# class KitchenTable(Table):
#     def setPlaces(self, p):
#         self.places = p
#  
# class DeskTable(Table):
#         def square(self):
#         return self.width * self.length

# class IncapsTest:
#     def__init__(self,value):
#         self.__privat_value = value

#     @property
#     def privat_value(self):
#             return self.__privat_value

#     @privat_value.setter
#     def privat_value(self, val):
#         return self.__privat_value = val
# P = IncapsTest(1234)
# # print(p.value)
# p.value = 43212
# print(p.value)

# class Point:
#     def __init__(self, *args):
#         self.__point = args

#     def get_(self):
#         return f'Point {self.__point}'



# p = Point(1,1,1)
# print(p.point)

# class My_Str:
#     def __init__(self, val):
#         self.val = val
#     def __add__(self, arg):
#         return f"{self.val}{arg}"
#     def __dir__(self):
#         print("nea")
#         return []
# s =My_Str('asdfgh')    
# import pdb; pdb.set_trace()

# class Count:

#     def __init__(self,start=10):
#         self.num = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.num+=1
#         return self.num

# n = Count(0)
# for i in n:
#     print(i)
#     break


# class CircumList:

#     def __init__(self, array):
#         self.array = array
#         self.to_show = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         i = self.to_show
#         self.to_show += 5
#         if self.to_show >= len(self.array):
#             self.to_show =self.to_show  % len(self.array)
#         return self.array[i]

# arr = CircumList([1,2,3,4,5,6,7,8])
# for x in arr:
#     import time
#     time.sleep(0.5)
#     print(x)



# from typing import AsyncIterable


class Window:

    def __init__(self, w, h):
        self.widht = w
        self.height= h

    @property
    def square(self):
        return self.widht*self.height

class Room:
    def __init__(self, w, h):
        self.widht = w
        self.height= h
        self.deep = d
        self.window = []

    @property
    def wall_square(self):
        p = (self.widht+self.deep)*2
        area = p * self.height

        for window in self.window:
        area -= window.square
        return area

    def add.window(self,h,w):
        self.windows.append(Window(w,h))

r = Room(10,20,30)
print(r.wall_square)
r.add_window(1,2)
print(r.wall_square)


    



