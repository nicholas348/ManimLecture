def series(x):
    try:#尝试执行程序
        return 1/(1-x)
    except x<=0 or x>=1:#有意外情况
        raise ValueError("x must be between 0 and 1")
    finally:#不管是否报错，均执行
        print("Calculation completed")