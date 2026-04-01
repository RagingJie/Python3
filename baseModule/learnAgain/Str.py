# 字符串类型
import time

var1 = 'hello python!'
print(var1)
print(var1[2])
print(var1[2:10])

print('字符串更新：', var1[:5] + " world!")

# 续行符
print('line1  \
      line2 \
      line3')

# 反斜杠符号
print("\\")

# 单引号
print("\'")

# 双引号
print("\"")

# 响铃
print("\a")

# 退格(Backspace)
print("hello \b world!\b")

# 空
print("\000")

# 换行
print("1\n2")

# 纵向制表符
print("hello \v world")

# 横向制表符
print("hello \t world")

# 回车，将 \r后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r后面的内容完全替换完成。
print("hello\rworld!")
print('google runoob taobao\r123456')

# 换页
print("hello \f world!")

# 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")

# 十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

# 其它的字符以普通格式输出
print("ot12lijher")

# 使用 \r 实现百分比进度：
print()
print('百分比进度：')
for i in range(101):  # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:4}%", end='', flush=True)
    time.sleep(0.01)
print()
print()

# * 重复输出字符串
print(var1 * 4)
# in 成员运算符 - 如果字符串中包含给定的字符返回True
if 'hell1' in var1:
    print('包含')
else:
    print('不包含')

# not in 成员运算符 - 如果字符串中不包含给定的字符返回True
if 'hell1' not in var1:
    print('不包含')
else:
    print('包含')

# 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法
print(r'\n')
print('\n')
print(R'\n')

# % 格式化字符串 - % 格式化字符串：%s 表示字符串，%d 表示数字，%f 表示浮点数，%c 表示字符，%x 表示十六进制数，%o 表示八进制数，%b 表示二进制数，%e 表示科学计数法，%g 表示科学计数法，%p 表示十六进制数，%n 表示输出的数字的个
print("hello %s" % "world")
print("我叫 %s ，今年 %d 岁了！" % ('猫神', 18))

# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
var3 = """
    这是一个多行实例
    多行字符串可以使用制表符
    tab(\t)
    也可以使用换行符 [\n    ]
"""
print(var3)
print()

# f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
print(f"hello {var1}")
print(f"我叫 {var1} ，今年 {var3} 岁了！")

print(f"{1 + 5}")
print()
# 在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果
var2 = 10
print(f"{9 + var2}")
print(f"{9+var2=}")

# 常用函数
cainiao = "https://www.runoob.com/python3/python3-string.html"
print(f"想看菜鸟教程(点击即可跳转网页)：{cainiao}")

# capitalize() 将字符串的第一个字符转换为大写
var = "hello python! today, I'm learning to it!";
print(var.capitalize())

# center(width, fillchar) 返回一个指定的宽度width，居中的字符串，fillchar 为填充的字符，默认为空格。
print(var.center(100,"="))

# replace(old, new [, max]) 把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次
print(var.replace("python", "java"))
