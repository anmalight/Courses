from random import choice
'''
class B(object, metaclass = type):
    pass

a = B()#instance

class Baz(object, metaclass = type):
    def test(self, test='123'):
        print("Answer", test)
class Baz2(object):
    pass

baz_instance = Baz()
baz_instance.test(test='456')

print(isinstance(baz_instance, Baz))
print(isinstance(baz_instance, Baz2))
print(isinstance(baz_instance, Baz) or isinstance(baz_instance, Baz2))
'''
# ---------------------------------
'''
def my_def(x): return x

my_type =  (
    1, 1.1, '1', ['1'], ('1',), {1}, {"1", 1}, None,
    my_def, type, object
)

if all(isinstance(item, object) for item in my_type):
    print('All is')
'''

# ---------------------------------
'''
class Test:
    class_attr = "class_attr value"#обычный атрибут, общий для всех классов
    _class_attr = "_class_attr value"
    __class_attr = "__class_attr value"

    def class_method(self):
        print("class_attr value")

    def _class_method(self):
        print("_class_attr value")

    def __class_method(self):
        print("__class_attr value")

test_instance = Test()
test_instance2 = Test()
print(test_instance.class_attr)
print(test_instance2.class_attr)
print(test_instance._class_attr)
print(test_instance2._class_attr)
print(test_instance._Test__class_attr)
print(test_instance2._Test__class_attr)

test_instance2 = Test()
print(test_instance2._class_method)
'''
# ---------------------------------
'''
class PregnancyTest:

    def make(self):
        choice_index = choice((0, 1))
        print(("|", "||")[choice_index])
class BrokenPregnancyTest:
    def make(self):
        choice_index = choice((0,1))
        print(("", "|||")[choice_index])

good_test = PregnancyTest()
good_test.make()
bad_test = BrokenPregnancyTest()
bad_test.make()

for test in [good_test, bad_test]:
    test.make()
'''
# ---------------------------------
'''
class Parent:
    test_atr = "test atr Parent"
    def test(self):
        print("Test from Parent")

class Child(Parent):
    # Если пееропределен, то получит отсюда
    # test_atr = "test atr Child"
    def test2(self):
        print("Test from Child")
class Child2(Child):
    pass

child_instance = Child()
child_instance.test()
child_instance.test2()
print(child_instance.test_atr)
isinstance(child_instance, Child)
print(issubclass(Child, Parent))
print(issubclass(Child, Parent) or issubclass(Child2,Child))
print(dir(child_instance))

print(Child2.mro())
print(Child.mro())
print(Parent.mro())

class MainClass:
    _test = "MainClass test"

    def get_test(self):
        print("Call from class", self.__class__)
        return self.__test


class SubClass(MainClass):
    __test = "SubClass test"

    def get_test(self):
        print("Call from class", selg.__class__)
        return self.__test


print(issubclass(MainClass, SubClass))
print(issubclass(SubClass, MainClass), end='\n\n')

print(MainClass.mro())
print(SubClass.mro())

print(MainClass.mro())
print(SubClass.mro())
'''
# ---------------------------------
# Множественное наследовние
'''
class A:
    pass


class B:
    pass


class D(B):
    pass


#Порядок важен. Иначе тот, который будет раньше
class C(A,D, B):
    pass


print(C.mro())
'''
'''
class GoodClass:
    def test(self, test1:str = "123", test2:str = "456") -> str:
        # return "Success"
        return f"{test1} {test2}"


instance_1 = GoodClass().test()

class BadClass:
    def test(self, test: str = "789"):
        raise Exception("Error inside class")


class ChildClass(BadClass, GoodClass): pass


child_instance = ChildClass()
print(ChildClass.mro())
try:
    child_instance.test(test="3211", test2="321")
except Exception:
    pass
'''

# ---------------------------------
'''
#строгий
from abc import ABC, abstractmethod

class MyAsstractClass(ABC):
    @abstractmethod
    def my_required_method(self):pass


class MainClass(MyAsstractClass):
    pass


main_instance = MainClass()
'''


'''
class AbstractClass2:
    def required_method(self):raise NotImplementedError

    def test(self):return True

class MainClass2(AbstractClass2):
    # def required_method(self):
    #     print("!@#$")
    pass

main_instance2 = MainClass2()
# main_instance2.required_method()
print(main_instance2.test())
'''

class Temperatures:
    def _calculation(self, first):
        pass

    def from_celsium_to_farhengeit(self, celsium):
        # return farhengeit
        pass
    def from_farhengeit_to_celsium(self, farhengeit):
        # return celsium
        pass

instance = Temperatures()
instance2 = Temperatures().from_celsium_to_farhengeit(123)
