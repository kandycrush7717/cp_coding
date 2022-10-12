'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:22 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/CHOPRT)
        Given two numerical values A and B you need to help chef in finding the relationship between them that is,

        First one is greater than second or, First one is less than second or, First and second one are equal.
    * Example :
        Input :
        3
        10 20
        20 10
        10 10
        Output:
        <
        >
        =
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        if a<b:
            sys.stdout.write('<\n')
        elif a>b:
            sys.stdout.write('>\n')
        elif a==b:
            sys.stdout.write('=\n')
