'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-07
    * Time : 12:16 a.m.
    * Question :(https://www.codechef.com/LP2TO301/problems/MAKEDIV3)
        Given an integer N, help Chef in finding an N-digit odd positive integer X such that X is divisible by 3 but not
        by 9.
        Note: There should not be any leading zeroes in X. In other words, 003 is not a valid 3-digit odd positive integer.
    * Example :
        Input :-
            3
            1
            2
            3
        Output :-
            3
            15
            123
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        x='3'+'0'*(n-2)+'3' if n>=2 else '3'
        sys.stdout.write(x+'\n')
