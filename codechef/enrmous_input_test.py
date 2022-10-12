'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 12:56 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/INTEST)
        The purpose of this problem is to verify whether the method you are using to read input data is sufficiently
        fast to handle problems branded with the enormous Input/Output warning. You are expected to be able to process
        at least 2.5MB of input data per second at runtime.
    * Example :
        Sample 1:
            Input
            7 3
            1
            51
            966369
            7
            9
            999996
            11
            Output
            4

'''
import sys
if __name__=='__main__':
    n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
    count=0
    for _ in range(n):
        t=int(sys.stdin.readline().rstrip('\n'))
        if t%k==0:
            count+=1
    sys.stdout.write(str(count)+'\n')
