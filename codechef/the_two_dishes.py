'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-17
    * Time : 6:59 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/MAX_DIFF)
        Chef wonders, what can be the maximum possible absolute difference between the tastiness of the two dishes.
        Can you help the Chef in finding the maximum absolute difference?
    * Example :
        Input :
            3
            3 1
            4 4
            2 3
        Output :
            1
            4
            1
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,s=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        maxi=-1
        for i in range(n+1):
            a=i
            b=s-i
            temp=abs(a-b)
            if 0<=b<=n and temp>maxi:
                maxi=temp
        sys.stdout.write(str(maxi)+'\n')