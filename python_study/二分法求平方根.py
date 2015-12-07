#encoding=utf-8
# __author__ = 'bohan'
def squartRoot(x,epsilon):
    """
    :param x: 你所要求的平方根的数，根据平方根的定义，必须大于0
    :param epsilon: 你所要求的精确度，必须大于等于0
    :return: the sqrt of x
    """
    assert x>=0,'x必须大于等于0，而不是'+str(x)  #错误处理
    assert epsilon>=0,'epsilon必须大于等于0而不是'+str(epsilon)
    low = 0
    high = max(x,1)
    guess = (low+high)/2.0
    ctr = 1
    while abs(guess**2-x)>epsilon and ctr<=100:
        if guess**2<x:
            low = guess
        else:
            high = guess
        guess=(low+high)/2.0
        ctr+=1
    assert ctr<=100,'溢出了'
    return guess

a=float(raw_input("请输入你所要求的数字"))
b=float(raw_input("请输入你所要求的精确度"))
print squartRoot(a,b)
