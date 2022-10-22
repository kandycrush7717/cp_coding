'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 11:33 a.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/PAWRI)
        Lately, Chef has been inspired by the "pawri" meme. Therefore, he decided to take a string S and change each
        of its substrings that spells "party" to "pawri". Find the resulting string.
    * Example :
        Input :
            3
            part
            partypartiparty
            yemaihuyemericarhaiauryahapartyhorahihai
        Output :
            part
            pawripartipawri
            yemaihuyemericarhaiauryahapawrihorahihai
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        s=s.replace('party','pawri')
        sys.stdout.write(s+'\n')