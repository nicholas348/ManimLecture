def series(x):
    try:
        return 1/(1-x)
    except x<=0 or x>=1:
        raise ValueError("x must be between 0 and 1")
    finally:
        print("Calculation completed")