import math
import random
from random import seed

# 数字类型
'''
Python 支持三种不同的数值类型：
  - 整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
  - 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
  - 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
'''

var_one = 213
var_two = 2.5
var_three = 0x20
print(var_one)
print(var_two)
print(var_three)

#  数字类型转换
print(int("89"))
print(float(213))
print(complex("23"))
print(complex(43, 5))

# 数字函数
print(abs(-987))  # 返回 x 的绝对值
print(math.ceil(8.1))  # 返回数字的上入整数，如math.ceil(4.1) 返回 5
# print(cmp(2,9))    # 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
print(math.exp(1))  # 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print(math.fabs(-5.23))  # 返回数字的绝对值
print(math.floor(8.23))  # 返回数字的下入整数，如math.floor(4.1) 返回 4
print(math.log(math.e))  # 返回 x 的自然对数，即以e为底的对数，如math.log(math.e) 返回 1.0
print(math.log10(1000))  # 10 的对数，如math.log10(1000) 返回 3.0
print(max(20, 345, 54, 987))  # 返回数字中的最大值
print(min(20, 345, 54, 987))  # 返回数字中的最小值
print(math.modf(88.667))  # 返回数字的小数部分和整数部分
print(pow(5, 3))  # 返回 x 的 y 次幂
print(math.sqrt(100))  # 返回 x 的平方根
print(round(5.2789, 3))  # 返回数字的截断，即去掉小数部分
print(math.trunc(5.2789))  # 返回数字的截断，即去掉小数部分
print()
print()

# 随机数函数
print(random.randint(1, 10))  # 随机生成下一个整数，它在[start, stop]范围内。
print(random.choice([2, 45, 65, 76832, 32456, 56, 5676, 2134]))  # 随机返回一个列表的元素。
print(random.random())  # 随机生成下一个实数，它在[0,1)范围内。
print(random.randrange(1, 10, 3))  # 随机生成下一个整数，它在[start, stop)范围内，且是start的倍数。]
print(random.uniform(1, 10))  # 随机生成下一个实数，它在[start, stop)范围内。]
list = [324, '324', 45, 6757, 657, 5634, 5, 3, '32jhjk']
random.shuffle(list)  # 将序列的所有元素随机排序
print(list)
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))   # 随机返回一个列表的若干元素，但返回的列表长度不超过 len(list)。
print(random.getrandbits(10))   # 随机返回一个长为 n 的二进制数。
seed(1)    # 设置随机数种子，使每次生成的随机数相同。
print(random.random())

# 三角函数
print(math.acos(0.3))   # 返回 x 的反余弦值，即 x 的弧度余弦值。
print(math.asin(0.3))   # 返回 x 的反正弦值，即 x 的弧度正弦值。
print(math.atan(0.3))   # 返回 x 的反正切值，即 x 的弧度正切值。
print(math.atan2(1, 2))  # 返回两个参数的弧度值，即 x 的弧度正切值。
print(math.cos(0.3)) # 返回 x 的余弦值。
print(math.hypot(3, 4)) # 返回 x 的平方根加上 y 的平方根。
print(math.sin(0.3)) # 返回 x 的正弦值。
print(math.tan(0.3)) # 返回 x 的正切值。
print(math.degrees(0.3)) # 返回 x 的角度值，即 x 的弧度值乘以 180/pi。
print(math.radians(0.3)) # 返回 x 的弧度值，即 x 的角度值乘以 pi/180。
print(math.degrees(math.pi / 2)) # 弧度值

# 数学常量
print(math.pi)
print(math.e)
