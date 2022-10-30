'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-30
    * Time : 3:22 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/CM164364)
        There are nn chocolates, and you are given an array of nn numbers where the ii-th number A_i is the flavour
        type of the ii-th chocolate. Sebrina wants to eat as many different types of chocolates as possible, but she
        also has to save at least xx number of chocolates for her little brother.

        Find the maximum possible number of distinct flavour types Sebrina can have.
    * Example :
        Input :
            3
            2 1
            1 2
            4 2
            1 1 1 1
            5 3
            50 50 50 100 100
        Output :
            1
            1
            2
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, k = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        len_a = len(set([int(x) for x in sys.stdin.readline().rstrip('\n').split()]))
        if n - len_a >= k:
            sys.stdout.write(str(len_a) + '\n')
        else:
            sys.stdout.write(str(len_a - (k - (n - len_a))) + '\n')
