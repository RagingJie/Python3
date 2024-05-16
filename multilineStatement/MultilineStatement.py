# 多行语句

# item_one = "你号"
# item_two = "马上"
# item_three = "就要废了"
item_one = 1
item_two = 3
item_three = 5

# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
total = item_one + \
        item_two + \
        item_three
print("total：", total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠
total = ['item_one', 'item_two',
         'item_three', 'item_four']

print("total2：", total)
