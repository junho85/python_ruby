class Class1(object):
    def method1(self): return 'm1'

c1 = Class1()
print(c1, c1.method1())

class Class3(Class1): # class3 는 class1 을 상속 받음
    def method2(self): return 'm2'

c3 = Class3()
print(c3, c3.method1()) # class3 는 class1 이 가지고 있던 method1 을 상속 받았음
print(c3, c3.method2())

class Class2(object):
    def method1(self): return 'm1'
    def method2(self): return 'm2'

c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())
