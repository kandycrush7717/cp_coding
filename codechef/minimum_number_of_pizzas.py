'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-24
    * Time : 5:19 p.m.
    * Question :(https://www.codechef.com/LP2TO301/problems/MINPIZZAS)
        Chef is throwing a party for his N friends. There is a pizza store nearby and he wants to buy pizza for his
        friends. Each pizza has exactly K slices. Chef's friends get sad if one gets more slices than the other.
        Also, Chef gets sad if there are some pizza slices left. More formally, suppose Chef buys P pizzas, then
        everyone is happy if and only if there is a way to distribute K⋅P slices between N friends.

        You need to find the minimum number of pizzas Chef has to buy to share all the slices among his friends so
        that none of his friends gets sad. Note that Chef hates pizza and doesn't take any slices.
    * Example :
        Input :
            3
            2 2
            2 3
            4 2
        Output :
            1
            2
            2
'''
import sys
from math import *
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        N,K=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        sys.stdout.write(str(lcm(N,K)//K)+'\n')
