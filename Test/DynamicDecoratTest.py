class decorator_test:

    def __init__(self):
        self.test(self.wrapper)
        self.wrapped_func()

    def wrapper(self, func):
        def wrapped(*args, **kwargs):
            print('wrapped')
            return func(*args, **kwargs)
        return wrapped

    
def test(funcM,func,param):
    @func(param)
    def wrapped_func():
        funcM()
    return wrapped_func

def func1(var):
    print('func1')
    
def Dec(var):
    print('Dec')
    
    
class Person(object):

    def __init__(self,func):

        print('初始化')

        self.__func=func

    def __call__(self, *args, **kwargs):

        print('前装饰器功能')

        self.__func( *args, **kwargs)

        print('后装饰器功能')

@Person
def test(a):
    print('原函数')
    print(a)

test(4)

print('...........')

test(3)