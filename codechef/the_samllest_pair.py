'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-01
    * Time : 12:28 a.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/SMPAIR)
        You are given a sequence a1, a2, ..., aN. Find the smallest possible value of ai + aj, where 1 ≤ i < j ≤ N.
    * Example :
        Input :-
            1
            4
            5 1 3 4
        Output :-
            4
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        mini=a[-1]
        ans=(10**9)+7
        for i in range(n-2,-1,-1):
            ans=min(ans,mini+a[i])
            mini=min(mini,a[i])
        sys.stdout.write(str(ans)+'\n')