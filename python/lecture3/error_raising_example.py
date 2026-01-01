def series(x):
    # 尝试执行程序
    try:

        #这里返回代码
        return 1/(1-x)

    # 有意外情况
    except x<=0 or x>=1:

        # 返回错误
        raise ValueError("x must be between 0 and 1")

    # 不管是否报错，均执行
    finally:
        print("Calculation completed")