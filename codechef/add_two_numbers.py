'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:17 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW001)
        The task is very simple: given two integers A and B, write a program to add these two numbers and output it.
    * Example :
        Input:
        3
        1 2
        100 200
        10 40
        Output:
        3
        300
        50
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        sys.stdout.write(str(a+b)+'\n')