'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 6:56 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/CSUB)
        Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
        In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N.
    * Example :
        Input :
            2
            4
            1111
            5
            10001
        Output :
            10
            3
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        s=sys.stdin.readline().rstrip('\n')
        count=0
        for i in s:
            if i=='1':
                count+=1
        ans=0
        for i in range(1,count+1):
            ans+=i
        sys.stdout.write(str(ans)+'\n')
