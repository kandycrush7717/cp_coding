'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-02
    * Time : 10:16 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/GUESS)
        Alice and Bob, both have to drink water. But they both don't want to go, so they will play a game to decide
        who will fetch water for both of them. Alice will choose a number randomly between 1 and N (both inclusive)
        and Bob will choose a number randomly between 1 and M (both inclusive). Both will write their numbers on a slip
        of paper. If sum of numbers choosen by both is odd, then Alice will go, else Bob will go.
        What is probability that Alice will go?
    * Example :
        Input :-
            3
            1 1
            1 2
            2 3
        Output :-
            0/1
            1/2
            1/2
'''
import sys
import math

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        N, M = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        N_odds = int(math.ceil(N / 2))
        N_evens = int(math.floor(N / 2))
        M_odds = int(math.ceil(M / 2))
        M_evens = int(math.floor(M / 2))
        num = (N * M) - (N_evens * M_evens) - (N_odds * M_odds)
        den = (N * M)
        gcd = math.gcd(num, den)
        num //= gcd
        den //= gcd
        print(str(num) + '/' + str(den))