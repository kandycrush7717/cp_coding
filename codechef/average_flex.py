'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 6:42 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/AVGFLEX)
        There are N students in a class, where the ii-th student has a score of A_i The i-th student will boast if and
        only if the number of students scoring less than or equal A_i is greater than the number of students scoring
        greater than A_i Find the number of students who will boast.
    * Example :
        Input :
            3
            3
            100 100 100
            3
            2 1 3
            4
            30 1 30 30
        Output :
            3
            2
            3
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        a.sort()
        i=n//2
        while(i>0 and a[i]==a[i-1]):
            i-=1
        ans=n-i
        sys.stdout.write(str(ans)+'\n')