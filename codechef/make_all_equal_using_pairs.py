'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-28
    * Time : 12:51 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/PAIREQ)
        Chef has an array AA of length NN.

        In one operation, Chef can choose any two distinct indices i,j (1≤i,j≤N,i!=j) and
        either change A_i to A_j or A_j to A_i

        Find the minimum number of operations required to make all the elements of the array equal.
    * Example :
        Input :
            4
            3
            1 2 3
            4
            5 5 5 5
            4
            2 2 1 1
            3
            1 1 2
        Output :
            2
            0
            2
            1
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        freq_dict={}
        for i in a:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1
        maxi=0
        for i in freq_dict:
            if maxi<freq_dict[i]:
                maxi=freq_dict[i]
        ans=n-maxi
        sys.stdout.write(str(ans)+'\n')
