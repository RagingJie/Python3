# 以下实例在变量赋值时 Number 对象将被创建
var1 = 1
var2 = 10

# 使用del语句删除一些数字对象的引用
# del var1[,var2[,var3[....,varN]]]
del var1
# print(var1)
print(var2)

number = 0xA0F  # 十六进制
print(10 * 16 ** 2 + 15)
print(number)

number = 0o37  # 八进制
print(3 * 8 ** 1 + 7)
print(number)

number = 5e2
print(float(5 * 10 ** 2))
print(number)

number = 3.14j  # 复数 = 实部 + 虚部（实数+虚数）
print(number)

x = 10
y = 20
number = complex(x, y)  # 拼接为复数
print(number)

result1 = 7 / 2
result2 = 7 // 2
print("result1=>", result1)
print("result2=>", result2)
