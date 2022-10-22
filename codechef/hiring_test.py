'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 6:18 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/HIRETEST)
        A company conducted a coding test to hire candidates. N candidates appeared for the test, and each of them
        faced M problems. Each problem was either unsolved by a candidate (denoted by 'U'), solved partially (denoted
        by 'P'), or solved completely (denoted by 'F').
        To pass the test, each candidate needs to either solve X or more problems completely, or solve (X−1) problems
        completely, and Y or more problems partially.
        Given the above specifications as input, print a line containing N integers. The ith integer should be 1 if the
        ith candidate has passed the test, else it should be 00.
    * Example :
        Input :
            3
            4 5
            3 2
            FUFFP
            PFPFU
            UPFFU
            PPPFP
            3 4
            1 3
            PUPP
            UUUU
            UFUU
            1 3
            2 2
            PPP
        Output :
            1100
            101
            0
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,m=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        x,y=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        ans=''
        for i in range(n):
            s=sys.stdin.readline().rstrip('\n')
            f_count=0
            p_count=0
            for j in s:
                if j=='F':
                    f_count+=1
                elif j=='P':
                    p_count+=1
            if f_count>=x or (f_count==x-1 and p_count>=y):
                ans+='1'
            else:
                ans+='0'
        sys.stdout.write(ans+'\n')
