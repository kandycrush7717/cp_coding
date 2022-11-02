'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-02
    * Time : 5:29 p.m.
    * Question :(https://leetcode.com/problems/contains-duplicate/)
        Given an integer array nums, return true if any value appears at least twice in the array, and return false
        if every element is distinct.
    * Example :
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true

        Input: nums = [1,2,3,4]
        Output: false
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a_set=set()
        flag=False
        for i in a:
            if i in a_set:
                flag=True
                break
            else:
                a_set.add(i)
        if flag:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
