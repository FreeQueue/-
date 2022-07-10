class A():
    def __init__(self):
        print("a")
    def call(self):
        print("b")
a=A
b= a()
b.call()