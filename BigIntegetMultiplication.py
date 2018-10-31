# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 下午2:57
# @Author  : Zijie Han
# @Site    : 
# @File    : BigIntegetMultiplication.py
# @Software: PyCharm
import math

class BigInteger(object):


    def mMultiplicate(self, a, b):

        n = int(max(len(a),len(b))/2)

        a_ = a[:len(a)-n]
        b_ = a[-n:]
        c_ = b[:len(b)-n]
        d_ = b[-n:]

        z2 = self.mMultiplicate(a_ ,c_)
        z0 = self.mMultiplicate(b_ ,d_)
        #z1 =

    @staticmethod
    def mMinus( a ,b ):
        if len(a) == 1 and len(b) == 1:
            m = int(a) - int(b)
            if m < 0:
                return str(10 + m),-1
            if m >= 0:
                return str(m),1
        if len(a) == 0:
            return str(0-int(b)),-1
        if len(b) == 0:
            return a,1

        n = math.ceil(min(len (a) , len (b)) / 2)

        a_ = a[:len(a)-n]
        b_ = a[-n:]
        c_ = b[:len(b)-n]
        d_ = b[-n:]

        low,low_flag = BigInteger.mMinus(b_,d_)
        high,high_flag = BigInteger.mMinus(a_,c_)

        if low_flag == -1:
            i = -1
            while high[i] == "0" and abs(i) <= len(a):
                i -= 1
            if abs(i) == len(a) - 1:
                newHigh = str(int(high[0]) -1)
                while i < -1:
                    newHigh += "9"
                    i += 1
                high = newHigh
            else:
                newHigh = int(high[i])-1
                high = str(newHigh)

        return high+low,high_flag



    @staticmethod
    def mAdd(a , b):
        if len(a) == 1 and len(b) == 1:
            m = int(a) + int(b)
            if m >= 10:
                return str(m - 10),1
            if m < 10:
                return str(m),0
        if len(a) == 0:
            return b,0
        if len(b) == 0:
            return a,0

        n = math.ceil(min(len (a) , len (b)) / 2)

        a_ = a[:len(a)-n]
        b_ = a[-n:]
        c_ = b[:len(b)-n]
        d_ = b[-n:]

        low,lowflag = BigInteger.mAdd(b_,d_)
        high,highflag = BigInteger.mAdd(a_,c_)

        if lowflag == 1:
            i = -1
            while high[i] == "9" and abs(i) < len(high):
                i-=1
            tem = int(high[i])
            newHigh = high[0:i-1] + str(tem+1)
            while i < -1:
                newHigh += "0"
                i+=1
            high = newHigh
        return high+low,highflag



if __name__ == '__main__':
    print(BigInteger.mMinus("1000","2"))







