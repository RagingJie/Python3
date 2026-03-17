import keyword

from baseModule.multilineStatement.MultilineStatement import item_one

print()
print("python关键字：")
print(keyword.kwlist)
print()

# 1.标识符：
#   - 第一个字符必须以字母（a-z, A-Z）或下划线 _ 。
#   - 标识符的其他的部分由字母、数字和下划线组成。
#   - 标识符对大小写敏感，count 和 Count 是不同的标识符。
#   - 标识符对长度无硬性限制，但建议保持简洁（一般不超过 20 个字符）。
#   - 禁止使用保留关键字，如 if、for、class 等不能作为标识符。

# 合法标识符：
age = 25  # 普通变量名，最常见
user_name = "Alice"  # 用下划线连接单词，清晰易读
_total = 100  # 下划线开头通常表示“内部使用”或“私有”
MAX_SIZE = 1024  # 全大写通常表示“常量”（固定不变的值）
# calculate_area()        # 函数名，动词+名词
# StudentInfo             # 类名，首字母大写（驼峰命名法）
# __private_var           # 双下划线开头，有特殊含义

# 非法标识符：
# 2nd_place = "silver"    # 错误：以数字开头
# user-name = "Bob"       # 错误：包含连字符
# class = "Math"          # 错误：使用关键字
# $price = 9.99          # 错误：包含特殊字符
# for = "loop"           # 错误：使用关键字

姓名 = "张三"  # 合法
π = 3.14159  # 合法


# 测试标识符是否合法
def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False


print(is_valid_identifier("_324"))  # True
print(is_valid_identifier("324"))  # False

# 2.注释
# Python中单行注释以 # 开头，实例如下：
# 第一个注释

# 多行注释可以用多个 # 号，还有 ''' 和 """：
# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

# 3.行与缩进
'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
'''
if True:
    print("True")
else:
    print("False")

# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#   print ("False")    # 缩进不一致，会导致运行错误

# 4.多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print("total：", total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['one', 'two',
         'three', 'four']
print("total：", total)

# 5.数字(Number)类型
'''
python中数字有四种类型：整数、布尔型、浮点数和复数。
    - int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    - bool (布尔), 如 True。
    - float (浮点数), 如 1.23、3E-2
    - complex (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j
'''
print(1 + 2j)

# 6.字符串(String)
tip = '''
    - Python 中单引号 ' 和双引号 " 使用完全相同。
    - 使用三引号可以指定一个多行字符串。
    - 转义符 \。
    - 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
    - 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
    - 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    - Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    - Python 中的字符串不能改变。
    - Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
    - 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
    - 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
'''
print(tip)

str = '123456789'
print(str)  # 输出字符串
print(str[0])  # 输出字符串第一个字符
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串
print('------------------------------')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 7.空行
'''
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是 Python 语法的一部分。书写时不插入空行，Python 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
'''

# 8.等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入：
name = input("请输入姓名：")
print("用户输入的姓名是：", name)

# 9.同一行显示多条语句
# - Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

# 10.多个语句构成代码组
'''
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
'''
if 1:
    print(1)
elif 2:
    print(2)
else:
    print(3)

# 11.print 输出
'''
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
'''
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

# 12.import 与 from...import
"""
 - 在 python 用 import 或者 from...import 来导入相应的模块。
 - 将整个模块(somemodule)导入，格式为： import somemodule
 - 从某个模块中导入某个函数,格式为： from somemodule import somefunction
 - 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
 - 将某个模块中的全部函数导入，格式为： from somemodule import *
"""
#导入 sys 模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import argv, path  # 导入特定的成员
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
