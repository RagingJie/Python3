counter = 100  # 整型变量
miles = 120.32  # 浮点型变量
name = "Runoob"  # 字符串变量

print(counter)
print(miles)
print(name)

# 同时为多个变量赋值
a = b = c = 10
print(a)
print(b)
print(c)

# 为多个对象指定多个变量
a, b, c = 10, '你好啊', 30.23098
d = True
print(a)
print(b)
print(c)

print()

print(type(a))
print(type(b))
print(type(c))
print(type(d))

arr = [1, 23, '23', 3.0]
print(type(arr))

# isinstance 和 type 的区别在于：
#   - type()不会认为子类是一种父类类型。
#   - isinstance()会认为子类是一种父类类型。
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, complex))

print(1 == True)
print(0 == False)

var1 = 1
var2 = 10
del var1  # del 语句删除单个或多个对象
# print(var1)  # NameError: name 'var1' is not defined. Did you mean: 'var2'?
print(var2)
print()
print('加减乘除!')
print(5 + 4)
print(23.5 - 4)
print(3 * 3)
print(2 / 4)  # 除法，得到一个浮点数
print(9 // 4)  # 除法，得到一个整数
print(123 % 4)  # 取余
print(2 ** 10)  # 乘方

print()

"""
与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。
注意：
1、反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。
2、字符串可以用 + 运算符连接在一起，用 * 运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""
print('字符串!')
str = 'Naruto-S'  # 定义一个字符串变量
print(str)  # 打印整个字符串
print(str[0:-1])  # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])  # 打印字符串的第一个字符
print(str[2:5])  # 打印字符串第三到第五个字符（不包含索引为 5 的字符）
print(str[2:])  # 打印字符串从第三个字符开始到末尾
print(str * 2)  # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起
print("转义字符")
print("你\t好\n啊")
print(r"你\t好\n啊")
print(str[:])

'''
bool（布尔类型）
    - 布尔类型即 True 或 False。
    - 在 Python 中，True 和 False 都是关键字，表示布尔值。
    - 布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。
    - 布尔类型特点：
    - 布尔类型只有两个值：True 和 False。
    - bool 是 int 的子类，因此布尔值可以被看作整数来使用，其中 True 等价于 1。
    - 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。
    - 布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。
    - 布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。
    - 可以使用 bool() 函数将其他类型的值转换为布尔值。以下值在转换为布尔值时为 False：None、False、零 (0、0.0、0j)、空序列（如 ''、()、[]）和空映射（如 {}）。其他所有值转换为布尔值时均为 True。
'''

# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))  # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))  # False
print(bool(42))  # True
print(bool(''))  # False
print(bool('Python'))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2)  # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
print()

'''
List（列表）
    - List（列表） 是 Python 中使用最频繁的数据类型。
    - 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
    - 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
    - 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
'''
print("列表!")
list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 定义一个列表
tinylist = [123, 'runoob']

print(list)  # 打印整个列表
print(list[0])  # 打印列表的第一个元素
print(list[1:3])  # 打印列表第二到第四个元素（不包含第四个元素）
print(list[2:])  # 打印列表从第三个元素开始到末尾
print(tinylist * 2)  # 打印tinylist列表两次
print(list + tinylist)  # 打印两个列表拼接在一起的结果


# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串!!!!!!!!
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

'''
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
'''
print()
print("元组!")
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
tup3 = (20)  # 如果不添加逗号，如下所示，它将被解释为一个普通的值而不是元组. 因为在没有逗号的情况下，Python会将括号解释为数学运算中的括号，而不是元组的表示。
print(tup1)
print(tup2)

print(type(tup1))
print(type(tup2))
print(type(tup3))

'''
Set（集合）
    - Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
    - 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
    - 在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
    - 另外，也可以使用 set() 函数创建集合。
    - 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。    
    
创建格式：
    parame = {value01,value02,...}
或者
    set(value)
'''
print()
print("set集合!")
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 1}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素

'''
Dictionary（字典）
    - 字典（dictionary）是Python中另一个非常有用的内置数据类型。
    - 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    - 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
    - 键(key)必须使用不可变类型。
    - 在同一个字典中，键(key)必须是唯一的。
'''
print()
print("字典!")
dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(dict1.values())
print(dict1.keys())

'''
构造函数 dict() 可以直接从键值对序列中构建字典如下：
'''
dictData = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dictData)

# 注意：
#   1、字典是一种映射类型，它的元素是键值对。
#   2、字典的关键字必须为不可变类型，且不能重复。
#   3、创建空字典使用 { }。

'''
bytes 类型
    - 在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。
    - 与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
    - bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。
    - 创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：
    - 此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。
    
    bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码.
'''
x = b"bbhello"
print(x)
y = x[1:2]
print(y)
z = x + b"world"
print(z)

x = b"hello"
if x[0] == ord("h"):   # 其中 ord() 函数用于将字符转换为相应的整数值。
    print("The first element is 'h'")

