# class O: ...
# class A(O): ...
# class B(O): ...
# class C(O): ...
# class D(O): ...
# class E(O): ...
# class K1(A, B, C): ...
# class K2(B, D): ...
# class K3(C, D, E): ...
# class Z(K1, K2, K3): ...
 
# print(Z.mro())

# class Horse:
 
#     def __init__(self):
#         print('init Horse')
#         pass
 
#     def ride(self):
#         print('ride')
 
# class Osyol:
 
#     def __init__(self):
#         print('init Osyol')
#         pass
 
#     def walk(self):
#         print('walk')
 
# class Myl(Osyol, Horse):
 
#     def __init__(self):
#         print('init Myl')
#         self.walk()
#         self.ride()
 
 
# m = Myl()
# m.ride()
# m.walk()


# def pprint(self):
#     print("hello")

# MyClass = type(
#     "MyClass",
#     (),
#     {
#         "atr":10,
#         "atr2":123,
#         "print":pprint,

#     }
# )
# m = MyClass()
# print(m.atr)
# m.print()
# # print(dir(m))


# class CheckHash:
 
#     def __init__(self, s):
#         self.string = s
 
#     def __hash__(self):
#         return len(self.string) * 10
 
#     def __eq__(self, s):
#         return s == self.string
 
 
# s = CheckHash('abcde')
# print(hash(s))


# class Parser:
 
#     def __init__(self, path):
#         self.path = path
#         self.file = open(self.path, 'r')
 
#     def __enter__(self):
#         return self
 
#     def __exit__(self, *args):
#         self.file.close()
 
#     def get_string(self):
#         string = self.file.readline()
#         return string.split(';')
 
#     def get_strings(self):
#         strings = self.file.readlines()
#         return [
#             s.split(';') for s in strings
#         ]
 
 
# with Parser('new_csv.csv') as p:
#     print(p.get_strings())

import sqlite3 as sql
 
 
class DBWorker:
    def __init__(self, db_name):
        self.cur_db = sql.connect(db_name)
        self.cursor = None
        self.result = None
 
    def connect_db(self):
        self.cursor = self.cur_db.cursor()
 
    def use_query(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.cur_db.commit()
 
    def return_result(self):
        return self.result
 
 
db = DBWorker('new_some.db')
db.connect_db()
# db.use_query("CREATE TABLE shop (id integer PRIMARY KEY, name varchar(60), location varchar(100));")
# db.use_query("CREATE TABLE product (id integer PRIMARY KEY, name varchar(60), cost float, shop_id integer);")
# 
# db.use_query('INSERT INTO shop(name, location) VALUES("EVROOPT", "MINSK")')