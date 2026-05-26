class java:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def f1(self):
        print("hello")
        self.c=5 
    @classmethod
    def f2(cls):
        cls.x=3
obj1=java(50,60)
obj1.f1()      
obj1.f1()
obj1.f2()
print()