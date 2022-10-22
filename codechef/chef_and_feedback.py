'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 5:38 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/ERROR)
        Lots of geeky customers visit our chef's restaurant everyday. So, when asked to fill the feedback form, these
        customers represent the feedback using a binary string (i.e a string that contains only characters '0' and '1'.
        Now since chef is not that great in deciphering binary strings, he has decided the following criteria to
        classify the feedback as Good or Bad :
        If the string contains the substring "010" or "101", then the feedback is Good, else it is Bad. Note that,
        to be Good it is not necessary to have both of them as substring.
        So given some binary strings, you need to output whether according to the chef, the strings are Good or Bad.
    * Example :
        Input :
            2
            11111110
            10101010101010
        Output :
            Bad
            Good
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        if '010' in s or '101' in s:
            sys.stdout.write('Good\n')
        else:
            sys.stdout.write('Bad\n')