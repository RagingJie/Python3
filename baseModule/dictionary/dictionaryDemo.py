# 字典
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }

tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict)  # 输出完整的字典

print(tinydict['likes'])
print(tinydict.get('url'))

# print(tinydict['aaa'])  # KeyError: 'aaa' 没有这个键时,会报错
tinydict['name'] =  'Naruto'
print(tinydict)

print()
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
# tinydict.clear()  # 清空字典
# del tinydict  # 删除字典
print('字典数据', tinydict)
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['Class']: ", tinydict['Class'])


# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

# 使用内建函数 dict() 创建字典：
emptyDict = dict()

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))


dictData = {'key1': 88.2, 'key2': 88.3, 'key3': 88.4}
print(dictData)
print(type(dictData))
data = str(dictData)
print(data)
print(type(data))

dataCopy = dictData.copy()
print(dataCopy)
newData = dictData.fromkeys(['key2', 'key1'])
print(newData)

newData1 = dictData.fromkeys(['key2', 'key1'], 20)
print(newData1)

if 'key2' in newData1:
    print('key2 存在')
else:
    print('key2 不存在')

print(dictData.items())
print(type(dictData.items()))
print(dictData.keys())
print(type(dictData.keys()))

dictData.setdefault('key3', 88)  # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(dictData)

dictData1 = {'2i': 123, 'ceshi': '123980'}
dictData1.update(dictData)
print(dictData1)

print(dictData1.values())

param = dictData1.pop('key11', None)
print(dictData1)
print(param)

item = dictData1.popitem()  # 返回并删除字典中的最后一对键和值。
print(dictData1)
print(item)


