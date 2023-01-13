'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-13
    * Time : 12:15 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/HIGHFREQ)
        Chef has an array A of length N.
        Let F(A) denote the maximum frequency of any element present in the array.
        For example:
        If A = [1, 2, 3, 2, 2, 1], then F(A) = 3 since element 2 has the highest frequency = 3.
        If A = [1, 2, 3, 3, 2, 1], then F(A) = 2 since highest frequency of any element is 2.
        Chef can perform the following operation at most once:
        Choose any subsequence S of the array such that every element of S is the same, say x. Then, choose an
        integer y and replace every element in this subsequence with y.
        Determine the minimum possible value of F(A) Chef can get by performing the given operation at most once.
    * Example :
        Input :
            3
            4
            1 2 1 2
            5
            1 1 1 1 1
            6
            1 2 2 1 2 2
        Output:
            2
            3
            2
'''
import sys
import math

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        count_dict={}
        for i in a:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1
        counts=list(count_dict.values())
        s_max=-1
        maxi=counts[0]
        for i in range(1,len(counts)):
            if counts[i]>maxi:
                s_max=maxi
                maxi=counts[i]
            elif counts[i]>s_max:
                s_max=counts[i]
        ans=max(s_max,int(math.ceil(maxi/2)))
        sys.stdout.write(str(ans)+'\n')