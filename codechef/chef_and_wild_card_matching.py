'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 12:01 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/TWOSTR)
        Chef wants to implement wildcard pattern matching supporting only the wildcard '?'. The wildcard character '?' can
        be substituted by any single lower case English letter for matching. He has two strings X and Y of equal length,
        made up of lower case letters and the character '?'. He wants to know whether the strings X and Y can be
        matched or not.
    * Example :
        Input :
            2
            s?or?
            sco??
            stor?
            sco??
        Output :
            Yes
            No
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s1=sys.stdin.readline().rstrip('\n')
        s2=sys.stdin.readline().rstrip('\n')
        flag=True
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]!='?' and s2[i]!='?':
                    flag=False
                    break
        if flag:
            sys.stdout.write('Yes\n')
        else:
            sys.stdout.write('No\n')