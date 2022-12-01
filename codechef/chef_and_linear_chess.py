'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-01
    * Time : 12:46 a.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/LINCHESS)
        Chef wants to play a game of linear chess on a one-dimensional board ― an infinite row of squares numbered
        by positive integers. In this game, he has a pawn, which is initially at a square K. There are also N other
        people (numbered 1 through N); Chef can choose one of them to play against. For each valid i, the i-th player
        would play in the following way:

        Take a pawn and place it on a square P_i Repeat the following move any number of times: move the pawn from
        its current square P_i squares forward, i.e. from a square ss, this player's pawn is moved to the square s+P_i

        If this player moves their pawn to the square with Chef's pawn, then Chef's pawn is captured and he loses the game.
        Unfortunately, Chef cannot move his pawn during the game, making him an easy target for other players. Given
        the starting positions of all N+1 players, find a player who can capture Chef's pawn in the smallest number
        of moves or determine that no player can capture his pawn.
    * Example :
        Input :-
            2
            4 6
            4 3 2 8
            4 7
            4 3 2 8
        Output :-
            3
            -1
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        p=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        ans=-1
        for i in p:
            if i<k and k%i==0:
                ans=max(ans,i)
        sys.stdout.write(str(ans)+'\n')
