# 在定义函数参数时，可以在形参的前面加*，该形参将获取所有的位置实参
# 它会将所有的实参保存在一个元组中
def fn(*args):
    print("args=", args)
    print("args type:", type(args))


# 带*形参和其他参数配合使用
def fn1(a, b, *args):
    print(a)
    print(b)
    print(args)


# 下面这两种写法可以，但是在传实参的时候要注意
def fn2(*args, a, b):
    print(a)
    print(b)
    print(args)


def fn3(a, *args, b):
    print(a)
    print(args)
    print(b)


if __name__ == "__main__":
    # 接收所有的位置参数
    fn(1, 2, 3, 4, 5)
    fn1(11, 12, 13, 14)
    # fn2(21, 22, 23, 24)  #这么传会报错
    fn2(21, 22, a=23, b=24)
    # fn3(21, 22, 23, 24)  #这么传会报错
    fn3(21, 22, 23, b=24)
