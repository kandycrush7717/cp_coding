'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 3:33 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/BALLOON)
        Chef is participating in an ICPC regional contest, in which there is a total of N problems (numbered 1 through N)
        with varying difficulties. For each valid i, the i-th easiest problem is problem A_i.After a team solves a
        problem, a balloon with a colour representing that problem is tied next to their desk. Chef is fond of colours
        in VIBGYOR, which are representative of the problems with numbers 1 through 7. The remaining problems have their
        own representative colours too.Find the minimum number of problems which Chef's team needs to solve in order to
        get all the balloons for problems 1 through 7 (and possibly some other balloons too) tied next to their desk,
        if you know that Chef's team knows the difficulties of all problems and solves the problems in increasing order
        of difficulty.
    * Example :
        Input :
            3
            7
            1 2 3 4 5 7 6
            8
            8 7 6 5 4 3 2 1
            9
            7 4 3 5 6 1 8 2 9
        Output :
            7
            8
            8
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        count=0
        ans=0
        for i in range(n):
            if count==7:
                break
            if 1<=a[i]<=7:
                ans=i+1
                count+=1
        sys.stdout.write(str(ans)+'\n')