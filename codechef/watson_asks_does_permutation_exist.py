'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 5:41 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/PERMEXIS)
        Watson gives an array A of N integers A1, A2, ..., AN to Sherlock. He wants Sherlock to reorganize the array
        in a way such that no two adjacent numbers differ by more than 1.
        Formally, if reorganized array is B1, B2, ..., BN, then the condition that
        | Bi - Bi + 1 | ≤ 1, for all 1 ≤ i < N(where |x| denotes the absolute value of x) should be met.
        Sherlock is not sure that a solution exists, so he asks you.
    * Example :
        Input :
            2
            4
            3 2 2 3
            2
            1 5
        Output :
            YES
            NO
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a.sort()
        flag=True
        for i in range(n-1):
            if abs(a[i]-a[i+1])>1:
                flag=False
                break
        if flag:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
