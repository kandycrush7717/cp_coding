'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-02
    * Time : 6:28 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/FILL01)
        Chef has to work on a project for the next N hours. He is given a work plan to do this, which is given to you
        as a binary string SS of length NN. S_i = 1 if Chef has to work on the project during the i-th hour,
        and S_i = 0 if Chef is free during the i-th hour.
        Chef would like to use some of his free time to take naps. He needs a minimum of K consecutive hours of free
        time to take a nap. What is the maximum number of naps that Chef can take during the next N hours?
        Note that it is allowed for one nap to immediately follow another, i.e, Chef can wake up from one nap and then
        immediately take another one (if he has enough free time to do so), and these will be counted as different naps.
    * Example :
        Input :-
            3
            4 1
            1010
            4 2
            0100
            11 3
            00100000001
        Output :-
            2
            1
            2
'''
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        len_N,K=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        N=sys.stdin.readline().rstrip('\n')
        sleep=0
        ans=0
        for i in N:
            if i=='0':
                sleep+=1
                if sleep%K==0:
                    ans+=1
                    sleep==0
            else:
                sleep=0
        sys.stdout.write(str(ans)+'\n')
