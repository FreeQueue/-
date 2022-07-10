class CNM:
    varInt = 0

    def __init__(self, a: int):
        self.varInt = a


class Test:
    varInt = 10
    varDic:dict
    varClass: CNM

    def __init__(self):
        self.varDic = dict()
        self.varClass=CNM(5)


t1 = Test()
# print("通过类访问类变量：varInt: {}, varList: {},varClass:{}".format(
#     Test.varInt, Test.varDic, Test.varClass.varInt))
print("通过实例变量访问类变量：varInt: {}, varList: {},varClass:{}".format(
    t1.varInt, t1.varDic, t1.varClass.varInt))
t1.varInt = 100
t1.varDic[0] = 10
print(t1.varDic)
t1.varClass = CNM(10)
t2 = Test()
# print("通过类访问类变量：varInt: {}, varList: {},varClass:{}".format(
#     Test.varInt, Test.varDic, Test.varClass.varInt))
print("通过实例变量访问类变量：varInt: {}, varList: {},varClass:{}".format(
    t1.varInt, t1.varDic, t1.varClass.varInt))
print(t2.varClass.varInt)
Test.varClass=8
print(Test.varClass)
t3=Test()
print(t2.varClass.varInt)
