'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-17
    * Time : 7:16 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/VDATES)
        Chef has taken his first dose of vaccine DD days ago. He may take the second dose no less than LL days and no
        more than RR days since his first dose.
        Determine if Chef is too early, too late, or in the correct range for taking his second dose.
    * Example :
        Input :
            4
            10 8 12
            14 2 10
            4444 5555 6666
            8 8 12
        Output :
            Take second dose now
            Too Late
            Too Early
            Take second dose now
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        d,l,r=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        if d<l:
            sys.stdout.write('Too Early\n')
        elif l<=d<=r:
            sys.stdout.write('Take second dose now\n')
        elif d>r:
            sys.stdout.write('Too Late\n')