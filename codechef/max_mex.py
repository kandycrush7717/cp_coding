'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-13
    * Time : 1:00 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/MEX)
        You are given a multi-set S of N integers, and an integer K. You want to find the maximum value of minimal
        excluded non-negative integer (MEX) of the multi-set given that you are allowed to add at most any K
        integers to the multi-set. Find the maximum value of MEX that you can obtain.

        Few examples of finding MEX of a multi-set are as follows. MEX of multi-set {0} is 1, {1} is 0, {0, 1, 3} is 2,
        {0, 1, 2, 3, 5, 6} is 4.
    * Example :
        Input :
            4
            3 0
            1 0 2
            3 1
            1 0 2
            4 3
            2 5 4 9
            2 0
            3 4
        Output :
            3
            4
            6
            0
'''
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        s=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        maxi=max(s)
        start=0
        req_nums=[]
        set_s=set(s)
        while(start<=maxi):
            if start not in set_s:
                req_nums.append(start)
            start+=1
        if k<len(req_nums):
            print(req_nums[k])
        else:
            print(maxi+1+k-len(req_nums))