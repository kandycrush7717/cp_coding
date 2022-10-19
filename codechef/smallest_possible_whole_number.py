'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-19
    * Time : 4:49 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/SMOL)
        You are given two integers NN and KK. You may perform the following operation any number of times
        (including zero): change NN to N-KN−K, i.e. subtract K from N. Find the smallest non-negative integer value
        of NN you can obtain this way.
    * Example :
        Input :
            3
            5 2
            4 4
            2 5
        Output :
            1
            0
            2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        if k==0:
            sys.stdout.write(str(n)+'\n')
        else:
            sys.stdout.write(str(n%k)+'\n')