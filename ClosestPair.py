# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 上午10:37
# @Author  : Zijie Han
# @Site    : 
# @File    : ClosestPair.py
# @Software: PyCharm
# 华中科技大学算法导论实验：最小点对问题
# Huazhong University of Sci & Tech Algotithms Experiment: The Closest Pair

import math

class Pair(object):
    def __init__(self,L = []):
        self.L = L
    #
    # 首先使用快速排序方式，将点对以X轴的坐标排序好
    # 函数 mQuickSort 和 mPartition 是将点对进行快速排序的算法
    # mQuickSort and mPartition quick sort the pairs(x , y) by x
    #
    def mQuickSort(self , p , r ):
        if p < r:
            q = self.mPartition(p , r)
            self.mQuickSort(p , q - 1)
            self.mQuickSort(q + 1 , r)
        return 0

    def mPartition(self , p , r ):
        x = self.L[r][0]
        i = p - 1
        j = p
        while j <= r - 1:
            if self.L[j][0] < x:
                i = i + 1
                t = self.L[i]
                self.L[i] = self.L[j]
                self.L[j] = t
            j += 1
        t = self.L[i+1]
        self.L[i+1] = self.L[r]
        self.L[r] = t
        return i + 1

    def getMinPairList(self, p , r):
        """

        :param p: 点对的左边界 (left border)
        :param r: 点对的右边界 (right border)
        :return: 最小点对距离，最小距离点对  (Distance, (Pair,Piar)
        """
        self.minDistance,tupple = self.closestPair(p,r)
        self.minPairList = []
        self.minPairList.append(self.L[tupple[0]])
        self.minPairList.append(self.L[tupple[1]])
        return self.minDistance,self.minPairList


    def closestPair(self, p , r):
        """

        :param p: 点对的左边界
        :param r: 点对的右边界
        :return: 最小的点对距离，最小点对元素下标
        """

        self.mQuickSort(0,len(self.L) - 1)
        x = int((p + r)/2)

        if x - p <= 3 or r - x <= 3:
            # When element num less than 3, Calculate the closest distance directly.
            # 当左右两边元素个数少于 3 时，直接计算最小点对。
            leftMin,leftPair = self.subClosest(p , x)
            rightMin,rightPair = self.subClosest(x , r)
            normalMin = 0
            normalPair = (0,0)
            if leftMin < rightMin:
                normalMin , normalPair = leftMin,leftPair
            else:
                normalMin , normalPair = rightMin,rightPair
        else:
            # To calculate the minimun pair of the left or right side
            # 计算左右两边的最小点对
            leftMin,leftPair = self.closestPair(p , x)
            rightMin,rightPair = self.closestPair(x , r)
            if leftMin < rightMin:
                normalMin = leftMin
                normalPair = leftPair
            else:
                normalMin = rightMin
                normalPair = rightPair

        # To calculate the minimum pair of the cross ones
        # 计算中间部分的最小点对
        tMiddleLeft = x - 1
        tMiddleRight = x + 1
        while self.L[x][0] - self.L[tMiddleLeft][0] < normalMin and tMiddleLeft > p:
            tMiddleLeft -= 1
        while self.L[tMiddleRight][0] - self.L[x][0] < normalMin and tMiddleRight < r:
            tMiddleRight += 1
        crossMin,crossPair = self.subClosest(tMiddleLeft,tMiddleRight)

        if crossMin < normalMin:
            normalMin = crossMin
            normalPair = crossPair

        return normalMin,normalPair

    def subClosest(self , p , r):
        i = p
        min = self.calDistance(p, r)
        minPair = (p , r)
        while i < r:
            j = i + 1
            while j <= r:
                t = self.calDistance(i,j)
                if t < min:
                    min = t
                    minPair = (i , j)
                j += 1
            i += 1
        return min,minPair


    def calDistance(self , x , y):
        a = self.L[x][0] - self.L[y][0]
        a = a*a
        b = self.L[x][1] - self.L[y][1]
        b = b*b
        return math.sqrt(a + b)


# if __name__ == '__main__':
#     L = [(7,5),(5,5),(2,2),(4,1),(100,8),(14,5),(6,7)]
#     mPair = Pair(L)
#     min,minPair = mPair.getMinPairList(0,len(L)-1)
#     print(mPair.L)
#     print(min)
#     print(minPair)
