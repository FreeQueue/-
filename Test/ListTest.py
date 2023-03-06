# a= [1,2,3]
# class B():
#     b:list
#     def copy(self,list:list):
#         self.b=list.copy()
# b=B()
# b.copy(a)
# print(a)
# print(b.b)
# b.b[0]=5
# print(a)
# print(b.b)


# c = {'a': 1, 'b': 2}
# d=iter(c)
# print(c)
# key=next(d)
# print(key,c[key])
# key=next(d)
# print(key,c[key])
# while True:
#     try:
#         print(next(d))
#     except:
#         d=iter(c.values())


# dic={1:"10",2:"20"}
# list=[1,2,3]
# def c(*args):
#     for i in args:
#         print(i)
b=list()
a=[]
a.append(b)
a.append(b)
print( len(a))