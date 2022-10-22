'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 5:15 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/MAGDOORS)
        Chef wants to cross a hallway of N doors. These N doors are represented as a string. Each door is initially
        either open or close, represented by 1 or 0 respectively. Chef is required to go through all the doors one
        by one in the order that they appear, starting from the leftmost door and moving only rightwards at each step.
        To make the journey easier, Chef has a magic wand, using which Chef can flip the status of all the doors
        at once. Determine the minimum number of times Chef has to use this wand to cross the hallway of doors.
    * Example :
        Input :
            3
            111
            010
            10011
        Output :
            0
            3
            2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        flips=0
        for i in s:
            if i=='0' and flips%2==0:
                flips+=1
            elif i=='1' and flips%2!=0:
                flips+=1
        sys.stdout.write(str(flips)+'\n')
