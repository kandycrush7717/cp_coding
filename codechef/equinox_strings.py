'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 7:22 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/EQUINOX)
        Sarthak and Anuradha are very good friends and are eager to participate in an event called Equinox. It is a
        game of words. In this game, NN strings S_1,...., S_N are given. For each string S_i if it starts with one
        of the letters of the word “EQUINOX”, Sarthak gets A points and if not, Anuradha gets B points. The one who has
        more points at the end of the game wins. If they both the same number of points, the game is a draw..
        Print the winner of the game, if any, otherwise print “DRAW”.
    * Example :
        Input :
            2
            4 1 3
            ABBBCDDE
            EARTH
            INDIA
            UUUFFFDDD
            2 5 7
            SDHHD
            XOXOXOXO
        Output :
            DRAW
            ANURADHA
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,a,b=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        sa=0
        an=0
        letters=set(list('EQUINOX'))
        for i in range(n):
            s=sys.stdin.readline().rstrip('\n')
            if s[0] in letters:
                sa+=a
            else:
                an+=b
        if sa==an:
            sys.stdout.write('DRAW\n')
        elif sa>an:
            sys.stdout.write('SARTHAK\n')
        elif an>sa:
            sys.stdout.write('ANURADHA\n')
