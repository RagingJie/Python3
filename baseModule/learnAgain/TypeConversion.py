# 数据类型转换

print("数字数据类型转换!")
num_int = 123
num_flo = 1.23

print("num_int的类型：",type(num_int))
print("num_flo的类型：",type(num_flo))

num_new = num_int + num_flo
print("num_new的值:", num_new)
print("num_new的类型：",type(num_new))

print()
print("字符串数据类型转换!")
param_num = 200
param_str = "900"
print("param_num的类型：",type(param_num))
print("param_str的类型：",type(param_str))

param_one = param_num + int(param_str)
print("param_one的值：", param_one)
print("param_one的类型：",type(param_one))

param_two = param_str + str(param_num)
print("param_two的值：", param_two)
print("param_two的类型：",type(param_two))
print()