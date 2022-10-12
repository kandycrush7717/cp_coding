'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 12:41 a.m.
    * Question :
        Write a program that accepts a number, n, and outputs the same.
    * Example :
        Sample Input
        123
        Sample Output
        123
'''
import sys
if __name__=='__main__':
    n=sys.stdin.readline().rstrip('\n')
    sys.stdout.write(str(n)+'\n')