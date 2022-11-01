'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-01
    * Time : 12:59 a.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/PUSH7PA)
        Pushpa has entered Chefland and wants to establish Pushpa-Raj here too.

        Chefland has N towers where the height of the i_th tower is H_i.To establish Pushpa-Raj, Pushpa does the
        following:

            Initially, Pushpa chooses any tower i (1≤i≤N) and lands on the roof of that tower.
            Let X denote the height of the tower Pushpa is currently on, then, Pushpa can land on the roof of any
            tower j (1≤j≤N) such that the height of the j_th tower is (X+1).
            Let i denote the index of the tower on which Pushpa lands, then, the height of all towers except tower i
            increases by 1 after each jump including the initial jump.

            To establish Pushpa-Raj, Pushpa wants to land at the maximum height possible. Determine the maximum
            height Pushpa can reach.
    * Example :
        Input :
            2
            4
            1 2 1 3
            1
            2
        Output :
            3
            2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        h=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        h_dict={}
        for i in h:
            if i in h_dict:
                h_dict[i]+=1
            else:
                h_dict[i]=1
        ans=0
        for i in h_dict:
            temp=i+(h_dict[i]-1)
            if temp>ans:
                ans=temp
        sys.stdout.write(str(ans)+'\n')