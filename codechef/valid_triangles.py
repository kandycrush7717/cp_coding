'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 5:49 p.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW013)
        Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the
        inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
    * Example :
        Input
        3
        40 40 100
        45 45 90
        180 1 1
        Output


        YES
        YES
        NO
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b,c=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        if (a+b+c)==180:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
