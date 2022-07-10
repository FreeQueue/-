from functools import wraps

def funcBase(var1,var2):
        # print(kwargs['var1'])
        # print(kwargs['var2'])
        print(var1)
        print(var2)
        
def DoubleDe(offset:int=3):
    def DoubleDe(func):
        @wraps(func)
        def DoubleDe(*args, **kwargs):
            for key in args:
                print("value:",key)
            # for key,value in kwargs:
            #     print("pair",key,value)
            kwargs['var2']+=1
            func(*args, **kwargs)
            func(*args, **kwargs)
        return DoubleDe
    return DoubleDe

def TripleDe(offset:int=3):
    def TripleDe(func):
        @wraps(func)
        def TripleDe(*args, **kwargs):
            func(*args, **kwargs)
            func(*args, **kwargs)
            func(*args, **kwargs)
        return TripleDe
    return TripleDe

def Make(func,Dec,var:int):
    @Dec(var)
    def R(*args, **kwargs):
        func(*args, **kwargs)
    return R

a=Make(funcBase,DoubleDe,5)
a(var1=1,var2=2)


# def Func(var=5):
#     print(var)
#     if(not var):
#         return
#     Func(var-1)

# def Func1(var=5):
#     print(1)
#     # if(not var):
#     #     return
#     # Func1(var-1)
#     # UnboundLocalError: local variable 'Func1' referenced before assignment
#     def Func1():
#         print(2)
#     Func1()



# class A():
#     def funcBase(self,var:int):
#         print(var)
        
#     def Decorator(self,func,Dec,param):
#         @Dec(param)
#         def R():
#             return func
#         return R
#     def Test(self):
#         a= self.Decorator(self.funcBase,TripleDe,5)
#         a(3)

# a=A()
# a.Test()
        
# class B(A):
#     @DoubleDe(5)
#     def funcBase(self,var: int):
#         return super().funcBase(var)

# class C(A):
#     @TripleDe(5)
#     @DoubleDe(5)
#     def funcBase(self,var: int):
#         return super().funcBase(var)
# class D(B):
#     @TripleDe(5)
#     def funcBase(self,var: int):
#         return super().funcBase(var)

# a=A()
# a.funcBase(3)
# print("------------")
# b=B()
# b.funcBase(3)
# print("------------")
# c=C()
# c.funcBase(3)
# print("------------")
# d=D()
# d.funcBase(3)