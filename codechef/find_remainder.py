'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:03 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW002)
        Write a program to find the remainder when an integer A is divided by an integer B.
    * Example :
        Input:
        3
        1 2
        100 200
        40 15
        Output:
        1
        100
        10
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        sys.stdout.write(str(a%b)+'\n')
