'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-12
    * Time : 11:34 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/NPAIRS)
        Given a string S of length N containing only numeric characters, find the number of Nice Pairs.
        A Nice Pair is a pair of indices -(i,j) such that 1≤i<j≤N and j - i = |S_j - S_i|
    * Example :
        Input:
            3
            3
            123
            5
            13492
            8
            94241234
        Output :
            3
            2
            9
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip('\n'))
        s = sys.stdin.readline().rstrip('\n')
        ans = 0
        for i in range(n):
            for j in range(i + 1, min(i + 10, n)):
                if j - i == abs(int(s[j]) - int(s[i])):
                    ans += 1
        sys.stdout.write(str(ans) + '\n')
