'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-20
    * Time : 10:46 p.m.
    * Question :
        Chef has three spells. Their powers are A, B, and C respectively. Initially, Chef has 00 hit points, and
        if he uses a spell with power P, then his number of hit points increases by P.
        Before going to sleep, Chef wants to use exactly two spells out of these three. Find the maximum number of hit
        points Chef can have after using the spells.
    * Example :
        Input :
            2
            4 2 8
            10 14 18
        Output :
            12
            32
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b,c=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        points=0
        points+=((a+b+c)-min(a,b,c))
        sys.stdout.write(str(points)+'\n')