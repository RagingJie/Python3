import random

# choice()
# 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
print("从0到9中随机挑选一个整数：", random.choice(range(10)))

# randrange()
# 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。
print("从 1-100 中选取一个奇数：", random.randrange(1, 100, 2))
print("从 0-99 选取一个随机数：", random.randrange(100))

# random()
# 随机生成下一个实数，它在[0,1)范围内。
print("随机生成下一个实数：", random.random())

# seed([x])
# x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
random.seed()
print("使用默认种子生成随机数：", random.random())
print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
print("使用字符串种子生成随机数：", random.random())

# shuffle(lst)
# 将序列的所有元素随机排序
list = [5, 2, 3, 181, 15, 26, 16, 4984, 168]
random.shuffle(list)
print("随机排序列表：", list)
random.shuffle(list)
print("随机排序列表：", list)

# uniform(x, y)
# 随机生成下一个实数，它在[x,y]范围内。
# x -- 随机数的最小值，包含该值。
# y -- 随机数的最大值，包含该值。
# 返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。
print("随机生成下一个实数，", random.uniform(5, 9))
