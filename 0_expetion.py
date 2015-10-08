# coding=utf-8
__author__ = 'bohan'
def reafFloat(requestMsg,errorMsg):
    while True:
        val = raw_input(requestMsg)
        try:
            val = float(val)
            return val
        except:
            print(errorMsg)
reafFloat(1,'a')