'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-30
    * Time : 11:46 p.m.
        * Question :(https://www.codechef.com/LP1TO204/problems/MAXDIFF)
        Chef has gone shopping with his 5-year old son. They have bought N items so far. The items are numbered from
        1 to N, and the item i weighs W_i grams.

        Chef's son insists on helping his father in carrying the items. He wants his dad to give him a few items.
        Chef does not want to burden his son. But he won't stop bothering him unless he is given a few items to carry.
        So Chef decides to give him some items. Obviously, Chef wants to give the kid less weight to carry.

        However, his son is a smart kid. To avoid being given the bare minimum weight to carry, he suggests that
        the items are split into two groups, and one group contains exactly K items. Then Chef will carry the heavier
        group, and his son will carry the other group.
    * Example :
        Input :-
            2
            5 2
            8 4 5 2 10
            8 3
            1 1 1 1 1 1 1 1
        Output :-
            17
            2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        w=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        w.sort(reverse=True)
        first_k_sum=sum(w[0:k])
        last_k_sum=sum(w[-1:(-1-k):-1])
        tot_sum=sum(w)
        f_son_wt=min(first_k_sum,tot_sum-first_k_sum)
        l_son_wt=min(last_k_sum,tot_sum-last_k_sum)
        son_wt=min(f_son_wt,l_son_wt)
        ans=abs(tot_sum-2*son_wt)
        sys.stdout.write(str(ans)+'\n')