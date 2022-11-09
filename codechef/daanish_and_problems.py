'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-09
    * Time : 12:11 p.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/DIV03)
        Daanish as always is busy creating and solving his favourite and interesting graph problems. Chef assigns each
        problem a difficulty — an integer between 1 and 10. For each valid i, there are A_i problems with difficulty i.

        A participant hacked Daanish's account and got access to the problem proposal document. He can delete up to
        K problems from the document in order to reduce the difficulty of the contest for himself and his friends.
        Find the smallest possible value of the difficulty of the most difficult problem which remains after removing
        K problems.
    * Example :
        Input :
            5
            1 10 1 5 3 2 4 9 0 100
            100
            2 0 1 0 0 0 0 0 0 10
            12
            2 0 1 0 0 0 0 10 0 0
            0
            2 0 1 0 0 0 0 0 0 10
            10
            1 10 1 5 3 2 4 9 0 100
            125
        Output :
            8
            1
            8
            3
            2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        arr=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        n=len(arr)
        k=int(sys.stdin.readline().rstrip('\n'))
        for i in range(n-1,-1,-1):
            k-=arr[i]
            if k<0:
                ans=(i+1)
                break
        sys.stdout.write(str(ans)+'\n')