# 列表

import operator

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d", 213, 2123, 43]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print(list1)
print(list2)
print(list3)
print(list4)

print(list1[0])
print(list1[-2])
print(list3[1:-2])
print(list3[2:6:2])

# 添加数据
list4.append('pink')
list4.append('purple')
print('更新后的数据列表：', list4)

# 删除数据
del list4[2]
del list4[3]
print('删除数据后的列表', list4)

# 长度
print(len(list4))
# 组合
print(list1 + list4)
# 重复
print(list4 * 4)
# 迭代
for item in list4:
    print(item, end=",")

print()  # end = ' ', 是不会换行

a = 'red'
if a in list4:
    print(a, '在列表中')
else:
    print(a, '不在列表中')

x = [1, 2, 3, 4, 5]
y = [4, 52, 6, 7, 8, 123, 3, 4, 65, 67, 3, 4, 5, 6, 5, 5, 5]
z = [1, 2, 3, 4, 5]

print('x与y是否相等：', operator.eq(x, y))
print('x与z是否相等：', operator.eq(x, z))

print(len(x))
print(max(y))
print(min(x))

x.append(y)
print(x)
# count 统计5在y中出现的次数
print(y.count(5))

# extend 扩展列表
y.extend(z)
print(y)

# index 查找元素, 返回元素第一次出现的索引
print(y.index(5))

# insert 插入元素
y.insert(2, 99)
print(y)

# pop 删除元素
y.pop(0)
print(y)

# remove 删除元素, 删除第一个匹配的元素
y.remove(5)
print(y)

# reverse 反转列表
y.reverse()
print(y)

# sort 排序
y.sort()
print(y)

# clear 清空列表
y.clear()
print(y)

# copy 复制列表
y = z.copy()
print(y)






