'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:49 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW004)
        If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.
    * Example :
        Input
        3
        1234
        124894
        242323
        Output
        5
        5
        5
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=sys.stdin.readline().rstrip('\n')
        fl_digit_sum=int(n[0])+int(n[-1])
        sys.stdout.write(str(fl_digit_sum)+'\n')

