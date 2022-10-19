'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-19
    * Time : 3:45 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/PROGLANG)
        Chef is a software developer, so he has to switch between different languages sometimes.
        Each programming language has some features, which are represented by integers here.
        Currently, Chef has to use a language with two given features AA and BB. He has two options ---
        switching to a language with two features A_1 and B_1 or to a language with two features A_2 and B_2.
        All four features of these two languages are pairwise distinct.
        Tell Chef whether he can use the first language, the second language or neither of these languages
        (if no single language has all the required features).

    * Example :
        Input :
            3
            1 2 2 1 3 4
            3 4 2 1 4 3
            1 2 1 3 2 4
        Output:
            1
            2
            0
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a, b, a1, b1, a2, b2 = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        one = [a1, b1]
        two = [a2, b2]
        if a in one and b in one:
            sys.stdout.write('1\n')
        elif a in two and b in two:
            sys.stdout.write('2\n')
        else:
            sys.stdout.write('0\n')
