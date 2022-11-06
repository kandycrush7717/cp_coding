'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-06
    * Time : 1:15 p.m.
    * Question :(https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/)
        You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
        You are also given an integer k.
        Pick the scores of any k students from the array so that the difference between the highest and the lowest
        of the k scores is minimized.
        Return the minimum possible difference.
    * Example :
        Input: nums = [9,4,1,7], k = 2
        Output: 2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        k=int(sys.stdin.readline().rstrip('\n'))
        nums.sort()
        i = 0
        j = k - 1
        mini = nums[-1]
        while (j < len(nums)):
            mini = min(mini, nums[j] - nums[i])
            i += 1
            j += 1
        sys.stdout.write(str(mini)+'\n')

