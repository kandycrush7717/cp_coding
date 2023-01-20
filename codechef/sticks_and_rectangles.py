'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-20
    * Time : 2:16 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/RECSTI)
        MoEngage has a bundle of NN sticks. The i_th stick has a length L_i meters.

        Find the minimum number of sticks (of any length) you need to add to the bundle such that you can construct
        some rectangles where each stick of the bundle belongs to exactly one rectangle and each side of a rectangle
        should be formed with exactly one stick.
    * Example :
        Input :
            4
            1
            1
            2
            2 5
            4
            2 2 3 3
            7
            1 3 5 7 1 7 5
        Output :
            3
            2
            0
            1
'''
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip())
        arr=[int(x) for x in sys.stdin.readline().rstrip().split()]
        count_dict={}
        req_stks=0
        for i in arr:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1
        for i in count_dict:
            rem_2=count_dict[i]%2
            if rem_2>0:
                req_stks+=(2-rem_2)
        rem_4=(n+req_stks)%4
        if rem_4>0:
            req_stks+=(4-rem_4)
        print(req_stks)