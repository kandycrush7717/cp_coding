'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-19
    * Time : 4:12 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/PROBCAT)
        Chef prepared a problem. The admin has rated this problem for xx points.
        A problem is called :
        Easy if 1≤x<100
        Medium if 100≤x<200
        Hard if 200≤x≤300
        Find the category to which Chef’s problem belongs.
    * Example :
        Input :
            3
            50
            172
            201
        Output :
            Easy
            Medium
            Hard
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        x=int(sys.stdin.readline().rstrip('\n'))
        if 1<=x<100:
            sys.stdout.write('Easy\n')
        elif 100<=x<200:
            sys.stdout.write('Medium\n')
        elif 200<=x<=300:
            sys.stdout.write('Hard\n')

