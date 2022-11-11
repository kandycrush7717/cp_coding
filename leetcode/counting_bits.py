'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-11
    * Time : 2:03 p.m.
    * Question :(https://leetcode.com/problems/counting-bits/)
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the
        number of 1's in the binary representation of i.
    * Example :
        Input: n = 5
        Output: [0,1,1,2,1,2]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        print(ans)
