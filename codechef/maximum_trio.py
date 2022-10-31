'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 5:23 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/MXMTRIO)
        You are given an array A of N elements. For any ordered triplet (i, j, k) such that i, j, and k are pairwise
        distinct and 1≤i,j,k≤N, the value of this triplet is (A_i-A_j)A_k.You need to find the maximum value among
        all possible ordered triplets.

        Note: Two ordered triplets (a, b, c) and (d, e, f) are only equal when a = d and b = e and c = f.
        As an example, (1, 2, 3) and (2, 3, 1) are two different ordered triplets.
    * Example :
        Input :
            3
            3
            1 1 3
            5
            3 4 4 1 2
            5
            23 17 21 18 19
        Output :
            2
            12
            126
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a.sort()
        max_val=(a[n-1]-a[0])*a[n-2]
        sys.stdout.write(str(max_val)+'\n')