# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 下午2:57
# @Author  : Zijie Han
# @Site    : 
# @File    : BigIntegetMultiplication.py
# @Software: PyCharm
import math

class BigInteger(object):

    @staticmethod
    def mMultiplicate(a, b):
        if b == "0":
            return "0"
        if b == "1":
            return a
        if len(a) <= 4 and len(b) <= 4:
            a_ = int(a)
            b_ = int(b)
            m = a_ * b_
            return str(m)

        if len(a) - len(b) >= 4:
            n = len(b)
            a_ = a[:len (a) - n]  #high
            b_ = a[-n:]           #low
            c_ = "0"
            d_ = b
        else:
            n = math.ceil(min(len(a),len(b))/2)
            a_ = a[:len (a) - n]  #high
            b_ = a[-n:]           #low
            c_ = b[:len (b) - n]
            d_ = b[-n:]

        z2 = BigInteger.mMultiplicate(a_,c_)
        z0 = BigInteger.mMultiplicate(b_,d_)
        a1 = BigInteger.Add(a_,b_)
        a2 = BigInteger.Add(c_,d_)
        z1_a = BigInteger.mMultiplicate(a1,a2)
        z1_b = BigInteger.Add(z2,z0)
        z1 = BigInteger.Minus(z1_a,z1_b)

        i = 0
        while i < n:
            z2 = z2+"00"
            z1 = z1+"0"
            i+=1

        return BigInteger.Add(z2,BigInteger.Add(z1,z0))




    @staticmethod
    def Minus(a,b):
        if a[0] == "-" and b[0] != "-":
            return "-"+BigInteger.Add(b,a[1:len(a)])
        if a[0] != "-" and b[0] == "-":
            return BigInteger.Add(a,b[1:len(b)])
        if a[0] == "-" and b[0] == "-":
            return BigInteger.Minus(b,a[1:len(a)])
        if(len(a) < len(b)):
            ans,ans_flag = BigInteger.mMinus(b,a)
            return "-"+ans
        elif(len(a) > len(b)):
            ans,ans_flag = BigInteger.mMinus(a,b)
            return ans
        else:
            while a[0] == b[0]:
                a = a[1:len(a)]
                b = b[1:len(b)]
            a,b,flag = BigInteger.handleMinusAns(a,b)
            ans , ans_flag = BigInteger.mMinus (a , b)
            if flag==-1:
                return "-"+ans
            return ans

    @staticmethod
    def handleMinusAns(a,b):
        n = len(a)
        i = 0
        while i < n:
            if int(a[i]) > int(b[i]):
                return a,b,1
            elif int(a[i]) < int(b[i]):
                return b,a,-1
            i+=1
        return a,b,1


    @staticmethod
    def mMinus( a , b ):
        if len(b) == 0:
            return a
        if len(a) <= 4 and len(b) <= 4:
            m = int(a) - int(b)
            if m < 0:
                flagNum = int(math.pow (10 , len(a)))
                numStr = str(m+flagNum)
                return numStr , -1
            elif m>0:
                numStr = str (m)
                length = len (numStr)
                i = 0
                while i < len(a) - length:
                    numStr = "0" + numStr
                    i += 1
                return numStr,1
            else:
                return "0000",0

        n = math.ceil(min((len(a),len(b))) / 2)

        a_ = a[:len(a) - n]
        b_ = a[-n:]
        c_ = b[:len(b) - n]
        d_ = b[-n:]

        low,low_flag = BigInteger.mMinus(b_,d_)
        high,high_flag = BigInteger.mMinus(a_,c_)

        if low_flag == -1 and high_flag != 0:
            newHigh = ""
            i = -1
            while high[i] == "0":
                newHigh = newHigh+"9"
                i -= 1
            newHigh = high[:len(high)+i]+str(int(high[i])-1)+newHigh
            return newHigh+low,high_flag
        elif low_flag == -1 and high_flag == 0:
            i = 0
            newHigh = ""
            while i <len(high):
                newHigh += "9"
                i+=1
            return newHigh+low,-1
        return high+low,high_flag


    @staticmethod
    def Add(a , b):
        if a[0] == "-" and b[0] != "-":
            return BigInteger.Minus(b,a[1:len(a)])
        if a[0] != "-" and b[0] == "-":
            return BigInteger.Minus(a,b[1:len(b)])
        if a[0] == "-" and b[0] == "-":
            return "-"+BigInteger.Add(a[1:len(a)],b[1:len(b)])
        if len(a) < len(b):
            ans,flag = BigInteger.mAdd(b,a)
        else:
            ans,flag = BigInteger.mAdd(a , b)
        if flag == 1:
            ans = "1"+ans
        return ans

    @staticmethod
    def mAdd(a , b):
        if len(b) == 0:
            return a,0
        if len(a) <= 4 and len(b) <= 4:
            m = int(a) + int(b)
            numStr = str(m)
            length = len(numStr)
            if length > len(a):
                numStr = numStr[1:len(numStr)]
                return numStr,1

            if length < len(a):
                i = 0
                while i < len(a) - length:
                    numStr = "0"+numStr
                    i+=1
                return numStr,0
            return numStr,0

        n = math.ceil(min(len (a) , len (b)) / 2)

        a_ = a[:len(a)-n]
        b_ = a[-n:]
        c_ = b[:len(b)-n]
        d_ = b[-n:]

        low,lowflag = BigInteger.mAdd(b_,d_)
        high,highflag = BigInteger.mAdd(a_,c_)

        if lowflag == 1:
            i = -1
            newHigh = ""
            while high[i] == "9" and abs(i) <= len(high):
                newHigh = "0"+newHigh
                i-=1
            if abs(i) == len(high):
                return newHigh+low,1
            else:
                newHigh = high[:len(high)+i]+str(int(high[i])+1)+newHigh
                return newHigh+low,highflag

        return high+low,highflag




if __name__ == '__main__':
    print(BigInteger.mMultiplicate("9223372036854775807","2"))







