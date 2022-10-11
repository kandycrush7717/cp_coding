'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-11
    * Time : 4:08 p.m.
    * Question : https://leetcode.com/problems/two-sum/
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
    * Example :
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
import sys
if __name__ == '__main__':
    nums = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
    target = int(sys.stdin.readline().rstrip('\n'))
    num_dict = {}
    n = len(nums)
    ans = []
    for i in range(n):
        compli = target-nums[i]
        if compli in num_dict:
            ans = [i, num_dict[compli]]
        num_dict[nums[i]] = i
    sys.stdout.write(str(ans))
