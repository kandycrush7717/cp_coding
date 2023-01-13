'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-12
    * Time : 8:48 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/CKWLK)
        You are playing EVE Online. Initially, you have one dollar, but you have somehow acquired two cheat codes.
        The first cheat code multiplies the amount of money you own by 10, while the second one multiplies it by 20.
        The cheat codes can be used any number of times.

        You want to have exactly N dollars. Now you are wondering: can you achieve that by only using some sequence
        of cheat codes?
    * Example :
        Input :
            4
            200
            90
            1000000000000
            1024000000000
        Output :
            Yes
            No
            Yes
            No
'''
import sys
import math

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip('\n'))
        pow_of_2 = 0
        pow_of_10 = 0
        while (n != 0 and n % 10 == 0):
            n //= 10
            pow_of_10 += 1
        while (n != 0 and n % 2 == 0):
            n //= 2
            pow_of_2 += 1
        if n == 1 and 0 <= pow_of_2 <= pow_of_10:
            sys.stdout.write('Yes\n')
        else:
            sys.stdout.write('No\n')
