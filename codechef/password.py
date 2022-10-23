'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 10:00 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/PASSWD)
        Chef is planning to setup a secure password for his Codechef account. For a password to be secure the following
        conditions should be satisfied:

        Password must contain at least one lower case letter [a-z][a−z];

        Password must contain at least one upper case letter [A-Z][A−Z] strictly inside, i.e. not as the first or
        the last character;

        Password must contain at least one digit [0-9][0−9] strictly inside;

        Password must contain at least one special character from the set \{{ '@', '#', '%', '&', '?' \}} strictly
        inside;

        Password must be at least 1010 characters in length, but it can be longer.

        Chef has generated several strings and now wants you to check whether the passwords are secure based
        on the above criteria. Please help Chef in doing so.
    * Example :
        Input :
            3
            #cookOff#P1
            U@code4CHEFINA
            gR3@tPWD
        Output :
            NO
            YES
            NO
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    spl = ['@', '#', '%', '&', '?']
    for _ in range(t):
        s = sys.stdin.readline().rstrip('\n')
        l = u = d = sp = False
        length = len(s) >= 10
        for i in range(len(s)):
            if s[i].islower():
                l = True
            elif s[i].isupper() and 1 <= i <= len(s) - 2:
                u = True
            elif s[i].isdigit() and 1 <= i <= len(s) - 2:
                d = True
            elif s[i] in spl and 1 <= i <= len(s) - 2:
                sp = True
        ans = 'YES' if length and l and u and d and sp else 'NO'
        sys.stdout.write(ans + '\n')

