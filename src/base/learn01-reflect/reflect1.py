"""
反射机制
    为什么会有反射机制：
        因为python是一种动态类型语言，我们在写、定义代码的时候，都是根据理想数据类型或者希望的数据类型进行编写的
        但是，当我们在执行代码的时候，并不知道该对象是否有我们定义时的属性或方法，所以我们就需要知道该对象是否有该属性或者方法属性
    主要方法:
        1.hasattr(): 判断该对象是否有某属性
        2.getattr(): 获取该对象某属性的值
        3.setattr()： 给对象添加某属性
        4.delattr(): 删除对象中的某属性
"""


class Person:
    head = '头是圆的'
    ears = '两个耳朵'
    eye = '两个眼睛'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f'This person name is {self.name}')

    def print_age(self):
        print(f'This person name is {self.age}')

    @classmethod
    def print_head(cls):
        print(f'classmethod: {cls.head}')

    @classmethod
    def print_ears(cls):
        print(f'classmethod: {cls.ears}')

    @classmethod
    def print_eye(cls):
        print(f'classmethod: {cls.eye}')

    @staticmethod
    def print_person():
        print(f'staticmethod: This is a person ... ')


xiao_ming = Person('xiaoming', 16)
# __dict__ -> dict: 返回 对象的实例数据属性
print(xiao_ming.__dict__)
print(Person.__dict__)
# dir() -> list: 返回对象所有属性，包括：实例(数据、方法)属性、类(数据、方法)属性
print(dir(xiao_ming))
print(dir(Person))  # 为什么通过 dir(类名) 也会返回 实例方法属性，却不返回实例数据属性?
# 为什么通过 dir(类名) 也会返回 实例方法属性?
#   因为我们可以通过 类名.实例方法属性(obj) 的方式对 obj对象 中的方法 进行调用;
#   却不可以通过 类名.实例数据属性名 的方式，对某一个实例的属性进行调用

# hasattr() -> bool: 该方法的依据就是：dir()方法
print('通过 实例对象 判断是否含有某些属性'.center(80, '-'))
print(f'xiao_ming has name attribute ? -->  ', hasattr(xiao_ming, 'name'))
print(f'xiao_ming has head attribute ? -->  ', hasattr(xiao_ming, 'head'))
print(f'xiao_ming has foot attribute ? -->  ', hasattr(xiao_ming, 'foot'))
print(f'xiao_ming has print_name attribute ? -->  ', hasattr(xiao_ming, 'print_name'))
print(f'xiao_ming has print_head attribute ? -->  ', hasattr(xiao_ming, 'print_head'))
print(f'xiao_ming has print_person attribute ? -->  ', hasattr(xiao_ming, 'print_person'))
print(f'xiao_ming has print_body attribute ? -->  ', hasattr(xiao_ming, 'print_body'))
print(f'xiao_ming has __delattr__ attribute ? -->  ', hasattr(xiao_ming, '__delattr__'))

print('通过 类名 判断是否含有某些属性'.center(80, '-'))
print(f'Person has name attribute ? -->  ', hasattr(Person, 'name'))
print(f'Person has head attribute ? -->  ', hasattr(Person, 'head'))
print(f'Person has foot attribute ? -->  ', hasattr(Person, 'foot'))
print(f'Person has print_name attribute ? -->  ', hasattr(Person, 'print_name'))
print(f'Person has print_head attribute ? -->  ', hasattr(Person, 'print_head'))
print(f'Person has print_person attribute ? -->  ', hasattr(Person, 'print_person'))
print(f'Person has print_body attribute ? -->  ', hasattr(Person, 'print_body'))
print(f'Person has __delattr__ attribute ? -->  ', hasattr(Person, '__delattr__'))

# getattr(): 获取属性的值。 如果是数据属性: 返回的是该数据属性的value ; 如果是 方法属性：返回的是该方法属性的内存地址
print('通过 实例对象 获取数据属性'.center(80, '-'))
print(f'xiao_ming get head attribute : {getattr(xiao_ming, "head")}')
print(f'xiao_ming get name attribute : {getattr(xiao_ming, "name")}')
print(f'xiao_ming get __delattr__ attribute : ', getattr(xiao_ming, '__delattr__'))


print('通过 实例对象 获取方法属性'.center(80, '-'))
print(f'xiao_ming get print_head attribute : ', getattr(xiao_ming, 'print_head'))
print(f'xiao_ming get print_name attribute : ', getattr(xiao_ming, 'print_name'))
print(f'xiao_ming get print_person attribute : ', getattr(xiao_ming, 'print_person'))
print(f'xiao_ming get __dict__ attribute : ', getattr(xiao_ming, '__dict__'))

print('通过 类名 获取数据属性'.center(80, '-'))
print(f'Person get head class data attribute : {getattr(Person, "head")}')
print(f'Person get name instance data attribute : {getattr(Person, "name", "没有该属性")}')
print(f'Person get __delattr__ private data  attribute : ', getattr(Person, '__delattr__'))

print('通过 类名 获取方法属性'.center(80, '-'))
print(f'Person get print_head class method attribute : ', getattr(Person, 'print_head'))
print(f'Person get print_name attribute : ', getattr(Person, 'print_name'))
print(f'Person get print_person attribute : ', getattr(Person, 'print_person'))
print(f'Person get __dict__ attribute : ', getattr(Person, '__dict__'))


# setattr()
def other_func01():
    print(f'this is other_func01 method .. ')


setattr(xiao_ming, 'other_fun01', other_func01)
print(hasattr(xiao_ming, 'other_fun01'))  # true
print(getattr(xiao_ming, 'other_fun01'))  # 证明通过setattr()方法set进实例对象中的方法是一个 普通(静态)方法

setattr(xiao_ming, 'other_attr01', "other_attr01")
print(hasattr(xiao_ming, 'other_attr01'))  # true
print(getattr(xiao_ming, 'other_attr01'))
print(xiao_ming.__dict__)


def other_func02(self):
    print(f'this is other_func02 method .. {self.other_attr01}')


setattr(xiao_ming, 'other_func02', other_func02)
getattr(xiao_ming, "other_func02")(xiao_ming)

