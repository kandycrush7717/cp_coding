'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-28
    * Time : 12:29 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/MATCHES)
        Chef's son Chefu found some matches in the kitchen and he immediately starting playing with them.

        The first thing Chefu wanted to do was to calculate the result of his homework — the sum of A and B, and
        write it using matches. Help Chefu and tell him the number of matches needed to write the result.
    * Example :
        Input :
            3
            123 234
            10101 1010
            4 4
        Output :
            13
            10
            7
'''
import sys
if __name__=='__main__':
    matches_dict={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        req_matches=0
        n=str(a+b)
        for i in n:
            req_matches+=(matches_dict[i])
        sys.stdout.write(str(req_matches)+'\n')
