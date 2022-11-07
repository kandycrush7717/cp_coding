'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-07
    * Time : 11:55 a.m.
    * Question :(https://leetcode.com/problems/3sum/)
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
        and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
    * Example :
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation:
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            low = i + 1
            high = n - 1
            while (low < high):
                k = target + nums[low] + nums[high]
                if k < 0:
                    low += 1
                elif k > 0:
                    high -= 1
                else:
                    ans.append((target, nums[low], nums[high]))
                    low += 1
                    high -= 1
                    while (low < high and nums[low] == nums[low - 1]):
                        low += 1
        print(ans)
