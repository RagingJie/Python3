# 数学函数
import math

number1 = 5
number2 = -5
number3 = 0
# abs(x): 返回数字的绝对值，如abs(-10) 返回 10
print("number1:", abs(number1))
print("number2:", abs(number2))
print("number3:", abs(number3))

# ceil(x): 返回数字的上入整数，如math.ceil(4.1) 返回 5
# 个人理解：向上取整
number = 15.26
print("number:", math.ceil(number))

# cmp(x, y): 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
# Python 3 已废弃，使用  替换
x = 10
y = 20
print("result:", (x > y) - (x < y))

# exp(x): 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print("exp(1):", math.exp(1))

# fabs(x): 以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0
number = -15.265
print("number:", math.fabs(number))

# floor(x): 返回数字的下舍整数，如math.floor(4.9)返回 4
# 向下取整
print("floor(5.915):", math.floor(5.915))

# log(x): 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print("log(25, 5)", math.log(25, 5))

print("math.log2(64):", math.log2(64))

# log10(x): 返回以10为基数的x的对数，如math.log10(100)返回 2.0
print("math.log10(1000):", math.log10(1000))

# min(x1, x2,...): 返回给定参数的最小值，参数可以为序列。
print("min(166,2626,155,6,45,15,62,15,54,52):", min(166, 2626, 155, 6, 45, 15, 62, 15, 54, 52))

# max(x1, x2,...): 返回给定参数的最大值，参数可以为序列。
print("max(1,5,2,56,15,55645,15,626,15,5):", max(1, 5, 2, 56, 15, 55645, 15, 626, 15, 5))

# modf(x): 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print("math.modf(5.21):", math.modf(5.21))

# pow(x, y): x**y 运算后的值。
print("pow(5,3):", pow(5, 3))

# round(x [,n]): 返回浮点数 x 的四舍五入值，如给出 n 值，。则代表舍入到小数点后的位数
# 其实准确的说是保留值将保留到离上一位更近的一端。
print("round(5.211314, 3):", round(5.211314, 3))

# sqrt(x): 返回数字x的平方根。
print("math.sqrt(10000):", math.sqrt(10000))
