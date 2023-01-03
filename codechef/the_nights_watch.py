'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-03
    * Time : 7:50 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/WTCH)
        There are N watchtowers built in a row. Each watchtower can only accommodate one person. Some of them are
        already occupied by members of the Night's Watch. Since the members of the Night's Watch do not get along,
        no two consecutive towers can be occupied at any moment.

        Arya heard that the wildlings are planning an attack. She is not satisfied by the current security, so she
        plans to place more members of the Night's Watch in the empty towers. What is the maximum number of people
        she can place in the towers such that no two consecutive towers are occupied afterwards? Note that Arya may
        not remove anyone from already occupied towers.
    * Example :
        Input :
            2
            6
            010001
            11
            00101010000
        Output :
            1
            3
'''
import sys
import math

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        s=sys.stdin.readline().rstrip('\n')
        s='10'+s+'01'
        ans=0
        strgt_0s=0
        for i in s:
            if i=='0':
                strgt_0s+=1
            else:
                strgt_0s-=2
                if strgt_0s>0:
                    ans+=int(math.ceil(strgt_0s/2))
                strgt_0s=0
        sys.stdout.write(str(ans)+'\n')