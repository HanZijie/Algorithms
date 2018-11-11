# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 下午2:57
# @Author  : Zijie Han
# @Site    : 
# @File    : BigIntegetMultiplication.py
# @Software: PyCharm
import math

class BigInteger(object):
    @staticmethod
    def Multiplicate(a , b):
        # 封装乘法函数
        
        ans = BigInteger.mMultiplicate(a , b)
        while ans[0] == "0":
            ans = ans[1:len(ans)]
        return ans

    @staticmethod
    def mMultiplicate(a, b):
        """
            未封装的乘法函数，它可能让最高位的返回值是 0 ，因为在乘法运算的过程中需要考虑字符串的长度对齐
        :param a: a str of first number
        :param b: a str of second number
        :return: a str of the result
        """
        if b == "0":
            return "0"
        if b == "1":
            return a
        if len(a) <= 4 and len(b) <= 4:
            # 进行计算
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


        # 分治 - Karatsuba算法

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
        """
            这是一个封装好的减法函数，它可以为减法分类，并对两个数字进行初步的处理：
        1. 比较两个数字的大小，总让大的减去小的。
        2. 在字符串长度相等的情况下，将两个数字高位相同的直接消去

        :param a: a str of the minuend
        :param b: a str of the subtractor
        :return: a str of the result
        """
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
            a,b,flag = BigInteger.handleMinusAns(a , b)
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
        """
            这是一个没有进行封装的减法函数，必须满足这个条件的条件：
            must satisfy: a > b

        :param a: a str of the minuend
        :param b: a str of the subtractor
        :return: a result(str} and a flag(a number in (1,-1))
                when flag = -1: borrow
        """
        if len(b) == 0:
            return a,1
        if len(a) <= 4 and len(b) <= 4:
            # 长度小于4时直接进行计算，可以提高效率，注意需要对齐字符串长度

            m = int(a) - int(b)
            if m < 0:
                flagNum = int(math.pow (10 , len(a)))
                numStr = str(m+flagNum)
                if(len(numStr) < len(a)):
                    i = 0
                    while i < len(a)-len(numStr):
                        numStr = "0"+numStr
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
                i = 0
                numStr = ""
                while i < len (a):
                    numStr = numStr + "0"
                    i += 1
                return numStr,0

        n = math.ceil(min((len(a),len(b))) / 2)

        a_ = a[:len(a) - n]
        b_ = a[-n:]
        c_ = b[:len(b) - n]
        d_ = b[-n:]

        low,low_flag = BigInteger.mMinus(b_,d_)
        high,high_flag = BigInteger.mMinus(a_,c_)

        if low_flag == -1 and high_flag != 0:
            # 处理借位：可参考 mAdd 函数中的详细注释

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
        """
            这是一个用于封装 mAdd 的函数，将加法根据值的不同，分情况讨论。
        :param a: str of a number
        :param b: str of a number
        :return: ans of a + b
        """
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
            # 根据最后是否有进位产生，决定首位是否加 1 。
            ans = "1"+ans
        return ans

    @staticmethod
    def mAdd(a , b):
        """
            这是一个没有进行封装的加法函数，必须满足这个条件，must satisfy: len(a)>len(b)

        :param a: a str of the first number
        :param b: a str of the second number
        :return: a result(str} and a flag(a number in (1,0))
                when flag = 1:carry-over
        """
        if len(b) == 0:
            return a,0
        if len(a) <= 4 and len(b) <= 4:
            # 当子字符串长度小于 4 时，执行加法运算，并根据运算结果，返回结果的字符串和 flag 。注意要让结果和字符串 a 的长度对齐！

            m = int(a) + int(b)
            numStr = str(m)
            length = len(numStr)
            if length > len(a):
                # 字符串对齐
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
            # 根据高低位的返回值进行进位计算，并向上返回
            i = -1
            newHigh = ""
            while high[i] == "9" and abs(i) < len(high):
                newHigh = "0"+newHigh
                i-=1
            if abs(i) == len(high):
                if high[i] == "9":
                    newHigh = "0" + newHigh
                    return newHigh+low,1
            else:
                newHigh = high[:len(high)+i]+str(int(high[i])+1)+newHigh
                return newHigh+low,highflag

        return high+low,highflag

def testMul1():
    a = "9223372036854775807"
    b = "1234567891111"
    print("乘法测试1：")
    print("我的计算结果："+a + "*" + b + "="+BigInteger.Multiplicate(a,b))
    print ("库的计算结果：" + a + "*" + b + "=" + str(int(a)*int(b))+"\n\n")

def testMul2():
    a = "11386878964471969137416693151577"
    a_ = 11386878964471969137416693151577
    print("乘法测试2：a=11386878964471969137416693151577")
    print("我的计算结果：a*a*a = "+BigInteger.Multiplicate(BigInteger.Multiplicate(a,a),a))
    print ("库的计算结果：a*a*a = "+str(a_*a_*a_)+"\n\n")

def testAdd():
    c = "1476434256335201019505915952536059041319057206399521214104693657122061789167297053187930937033"
    c_ = 1476434256335201019505915952536059041319057206399521214104693657122061789167297053187930937033
    print("加法测试：c = "+c)
    print("我的计算结果：c + c = "+BigInteger.Add(c,c))
    print ("库的计算结果：c + c = " + str(c_+c_)+"\n\n")

def testSub():
    d_ = 1476434256335201019505915952536059041319057206399521214104693657122061789167297053187930937033
    d = "1476434256335201019505915952536059041319057206399521214104693657122061789167297053187930937033"
    e_ = 2952868512670402039011831905072118082638114412799042428209387314244123578334594106375861874066
    e = str(e_)
    print("减法测试："+ d + '-'+ e)
    print("我的计算结果：d - e = "+BigInteger.Minus(d,e))
    print("库的计算结果：d - e = "+str(d_-e_)+"\n\n")

if __name__ == '__main__':
    testMul1()
    testMul2()
    testAdd()
    testSub()


