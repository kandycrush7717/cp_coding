'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-17
    * Time : 6:31 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/CHFRICH)
        Chef aims to be the richest person in Chefland by his new restaurant franchise. Currently,
        his assets are worth AA billion dollars and have no liabilities. He aims to increase his assets by XX billion
        dollars per year.

        Also, all the richest people in Chefland are not planning to grow and maintain their current worth.

        To be the richest person in Chefland, he needs to be worth at least BB billion dollars. How many years will
        it take Chef to reach his goal if his value increases by XX billion dollars each year?
    * Example :
        Input :
            3
            100 200 10
            111 199 11
            190 200 10
        Output :
            10
            8
            1
'''
import sys
import math
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b,x=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        balance=b-a
        ans=0
        if balance>0:
            ans=int(math.ceil(balance/x))
            sys.stdout.write(str(ans)+'\n')
        else:
            sys.stdout.write('0\n')