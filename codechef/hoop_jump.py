'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-19
    * Time : 2:27 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/HOOPS)
        You and your friend are playing a game with hoops. There are NN hoops (where NN is odd) in a row.
        You jump into hoop 11, and your friend jumps into hoop NN. Then you jump into hoop 22, and after that,
        your friend jumps into hoop N-1N−1, and so on.

        The process ends when someone cannot make the next jump because the hoop is occupied by the other person.
        Find the last hoop that will be jumped into.
    * Example :
        Input :
            2
            1
            3
        Output :
            1
            2

'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        sys.stdout.write(str((n//2)+1)+'\n')