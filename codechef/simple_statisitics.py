'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 3:35 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/SIMPSTAT)
        Sergey has made N measurements. Now, he wants to know the average value of the measurements made.
        In order to make the average value a better representative of the measurements, before calculating the
        average, he wants first to remove the highest K and the lowest K measurements. After that, he will calculate
        the average value among the remaining N - 2K measurements.
        Could you help Sergey to find the average value he will get after these manipulations?
    * Example :
        Input :
            3
            5 1
            2 9 -10 25 1
            5 0
            2 9 -10 25 1
            3 1
            1 1 1
        Output :
            4.000000
            5.400000
            1.000000
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a.sort()
        mean=0
        for i in range(k,n-k):
            mean+=a[i]
        mean/=(n-(2*k))
        sys.stdout.write('{m:.6f}'.format(m=mean)+'\n')