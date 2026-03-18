# 运算符

# 1、算术运算符
a = 10
b = 5
print("a = ", a)
print("b = ", b)
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)  # 取模 - 返回除法的余数
print("a // b = ", a // b)  # 取整除 - 往小的方向取整数
print("a ** b = ", a ** b)  # 幂 - 返回x的y次幂
print()
print()

# 2、比较运算符
c = 10
d = 5
print("c = ", c)
print("d = ", d)
print("c > d is ", c > d)
print("c < d is ", c < d)
print("c == d is ", c == d)
print("c != d is ", c != d)
print("c >= d is ", c >= d)
print("c <= d is ", c <= d)
print()
print()

# 3、赋值运算符
e = 10
f = 5
print("e = ", e)
print("f = ", f)
e += f
print("e += f is", e)
e -= f
print("e -= f is", e)
e *= f
print("e *= f is", e)
e /= f
print("e /= f is", e)
e %= f
print("e %= f is", e)
e = 10
f = 5
e //= f
print("e //= f is", e)
e = 10
f = 5
e **= f
print("e **= f is", e)
if (e := 2) > 5:
    print("e > 5")
print("e is", e)
print()
print()

# 4、位运算符
'''
二进制
a = 0011 1100      十进制：60
b = 0000 1101      十进制：13
c = 0000 0000      十进制：0  
'''
a = 60
b = 13
c = 0

c = a & b
print("&：按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0")
print("a & b = ", c)
print()
c = a | b
print("|：按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。")
print("a | b = ", c)
print()
print("^：按位异或运算符：对应的二进位相异时结果位为1，否则为0。")
c = a ^ b
print("a ^ b = ", c)  # 0011 0001   print(2**5+2**4+1)
print()
print("~：按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1 ")
c = ~a
print("~a = ", c)  # 1100 0011
print()
print("<<：左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数指定移动的位数，高位丢弃，低位补0。")
c = a << 2
print("a << 2 = ", c)  # 1111 0000  print(2**7+2**6+2**5+2**4)
print()
print(">>：右移动运算符：把 >> 左边的运算数的各二进位全部右移若干位， >>  右边的数指定移动的位数")
c = a >> 2
print("a >> 2 = ", c)  # 0000 1111  1+2+4+8
print()

# 5、逻辑运算符
a = 50
b = 10
print("a = ", a)
print("b = ", b)

if (a and b):
    print("a and b is true")
else:
    print("a and b is false")

if (a or b):
    print("a or b is true")
else:
    print("a or b is false")

if (not a):
    print("a is not true")
else:
    print("a is true")

# 6、成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5, 10]

if (a in list):                     # 如果在指定的序列中找到值返回 True，否则返回 False。
    print("a in list")
else:
    print("a not in list")

if (b not in list):                 # 如果在指定的序列中没有找到值返回 True，否则返回 False。
    print("b not in list")
else:
    print("b in list")

# 7、身份运算符
'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
a = 10
b = 10
print("a is b => ", a is b)

if ( id(a) == id(b) ):
   print ("a 和 b 有相同的标识")
else:
   print ("a 和 b 没有相同的标识")

b = 2
if(a is not b):
    print("a 和 b 没有相同的标识")
else:
    print("a 和 b 有相同的标识")

# 8、运算符优先级
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)

e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)

e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)


