def series(x):
    # 尝试执行程序
    #1+x+x^2+...=1/(1-x)
    try:

        #这里返回代码
        return 1/(1-x)

    # 有意外情况
    except x<=-1 or x>=1:

        # 返回错误
        raise ValueError("x must be between 0 and 1")

    # 不管是否报错，均执行
    finally:
        print("Calculation completed")