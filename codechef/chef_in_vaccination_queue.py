'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 1:47 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/VACCINQ)
        There are NN people in the vaccination queue, Chef is standing on the Pth position from the front of the queue.
        It takes X minutes to vaccinate a child and Y minutes to vaccinate an elderly person. Assume Chef is an elderly
        person.You are given a binary array A_1, A_2,...., A_N of length N, where A_i = 1 denotes there is an elderly
        person standing on the i th position of the queue, A_i = 0 denotes there is a child standing on the ith position
        of the queue. You are also given the three integers P,X,Y. Find the number of minutes after which Chef's
        vaccination will be completed.
    * Example :
        Input :
            3
            4 2 3 2
            0 1 0 1
            3 1 2 3
            1 0 1
            3 3 2 2
            1 1 1
        Output :
            5
            3
            6
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,p,x,y=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        time=0
        for i in range(p):
            if a[i]==1:
                time+=y
            elif a[i]==0:
                time+=x
        sys.stdout.write(str(time)+'\n')
