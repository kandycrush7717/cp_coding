'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-20
    * Time : 5:51 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/DENSE)
        A bracket sequence S is called dense if one of the following is true:
        SS is empty.
        S = (X) where X is dense.
        You are given a bracket sequence S. What is the minimum number of brackets you must remove to make it dense?
    * Example :
        Input :
            4
            8
            ()(())()
            6
            ((()))
            10
            ()()()()()
            8
            ((()))()
        Output :
            2
            0
            4
            2
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        s = sys.stdin.readline().rstrip()
        l = 0
        r = n - 1
        rm = 0
        while (l <= r):
            if s[l] != '(':
                while (l < n and l <= r and s[l] != '('):
                    rm += 1
                    l += 1
            elif s[r] != ')':
                while (r >= 0 and l <= r and s[r] != ')'):
                    rm += 1
                    r -= 1
            else:
                l += 1
                r -= 1
        print(rm)