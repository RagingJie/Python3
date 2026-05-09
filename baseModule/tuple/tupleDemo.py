# 元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以

print(tup1)
print(tup2)
print(tup3)

print(tup1[0])
print(tup1[1:3])
print(tup1[2:])

# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
tup5 = (1)
print(tup5)
print(type(tup5))  # <class 'int'>

tup6 = (1,)
print(tup6)
print(type(tup6))  # <class 'tuple'>

print(tup1 + tup2)
print(tup1 + tup3)
print(tup1 + tup3)

# 删除元组
del tup1
# print(tup1)  # 报错，因为tup1已经被删除，NameError: name 'tup1' is not defined. Did you mean: 'tup2'?
# 其余的函数用法与列表没有什么区别


# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
tupX = (213, 23, 'duiw', '你好啊', [12, 4, "nidwa"])
print(tupX)
print(id(tupX))  # 打印元组的id,即内存地址

tupX = ('你好啊', [888, "哈哈哈哈"])
print(tupX)
print(id(tupX))  # 内存地址不一样了
