'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 12:08 a.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/CSTOCK)
        Chef wants to buy a stock whose price was S rupees when the market opened. He will buy the stock if and only
        if its price is in the range [A,B]. The price of the stock has changed by C% by the time he was trying
        to buy the stock. Will he be able to buy the stock?
    * Example :
        Input :
            3
            100 93 108 7
            100 94 100 -7
            183 152 172 -17
        Output :
            Yes
            No
            No
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s,a,b,c=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        res=s+(s*c/100)
        if a<=res<=b:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
