'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-28
    * Time : 1:59 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/CFRTEST)
        Devu has n weird friends. Its his birthday today, so they thought that this is the best occasion for
        testing their friendship with him. They put up conditions before Devu that they will break the friendship
        unless he gives them a grand party on their chosen day. Formally, ith friend will break his friendship if he
        does not receive a grand party on d_ith day.

        Devu despite being as rich as Gatsby, is quite frugal and can give at most one grand party daily. Also,
        he wants to invite only one person in a party. So he just wonders what is the maximum number of friendships
        he can save. Please help Devu in this tough task !!
    * Example :
        Input :
            2
            2
            3 2
            2
            1 1
        Output :
            2
            1
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        d=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        s=set(d)
        ans=len(s)
        sys.stdout.write(str(ans)+'\n')
