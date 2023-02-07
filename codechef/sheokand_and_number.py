'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-07
    * Time : 1:28 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/SHKNUM)
        Sheokand is good at mathematics. One day, to test his math skills, Kaali gave him an integer N. To impress Kaali,
        Sheokand has to convert N into an integer M that can be represented in the form 2^x +2^y(where
        x and y are non-negative integers such that x!=y). In order to do that, he can perform two types of operations:

            add 1 to N
            subtract 1 from N
        However, Sheokand is preparing for his exams. Can you help him find the minimum number of operations required
        to convert N into a valid integer M?
    * Example :
    Input :
        3
        10
        22
        4
    Output :
        0
        2
        1
'''
import sys
import math

if __name__=='__main__':
    bounds=[]
    for i in range(31):
        for j in range(i+1,31):
            b=(1<<i)+(1<<j)
            bounds.append(b)
    t=int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip())
        ans=(10**9)+7
        for i in bounds:
            ans=min(ans,abs(i-n))
        print(ans)
