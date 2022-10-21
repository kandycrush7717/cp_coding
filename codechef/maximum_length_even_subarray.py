'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 12:31 a.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/MXEVNSUB)
        You are given an integer NN. Consider the sequence containing the integers 1,2,…,N in increasing order
         (each exactly once). Find the maximum length of its contiguous subsequence with an even sum.
    * Example :
        Input :
            3
            3
            4
            5
        Output :
            3
            4
            4
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip('\n'))
        temp = 0
        if n & 1 != 0:
            temp = n + 1
        else:
            temp = n
        if (temp >> 1) & 1 != 0:
            sys.stdout.write(str(n - 1) + '\n')
        else:
            sys.stdout.write(str(n) + '\n')
