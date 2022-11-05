'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-04
    * Time : 11:51 p.m.
    * Question :(https://leetcode.com/problems/longest-consecutive-sequence/)
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    * Example :
        Input: nums = [100,4,200,1,3,2]
        Output: 4
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.stdin.readline().rstrip('\n')]
        num_set = set(nums)
        max_len = 0
        for i in num_set:
            if i - 1 not in num_set:
                current = i
                curr_len = 1
                while (current + 1 in num_set):
                    current += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        sys.stdout.write(str(max_len)+'\n')