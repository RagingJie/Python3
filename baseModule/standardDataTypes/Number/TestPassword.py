import random
import string

def generate_password(length):
    # 定义密码可用字符集合
    chars = string.ascii_letters + string.digits + string.punctuation

    # 大小写
    print(string.ascii_letters)
    # 数字
    print(string.digits)
    # 标点
    print(string.punctuation)

    # 随机选择字符生成密码
    password = ''.join(random.choice(chars) for _ in range(length))

    return password
random_pwd = generate_password(4) # 输出长度为 6
print(random_pwd)