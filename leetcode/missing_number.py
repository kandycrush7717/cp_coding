'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-11
    * Time : 2:54 p.m.
    * Question :(https://leetcode.com/problems/missing-number/)
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
        that is missing from the array.
    * Example :
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number
        in the range since it does not appear in nums.
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.sttdin.readline().rstrip('\n')]
        index_xor=0
        num_xor=0
        for i in range(1,len(nums)+1):
            index_xor^=i
            num_xor^=nums[i-1]
        missing = index_xor ^ num_xor
        sys.stdout.write(str(missing)+'\n')
'''
        Other Way
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.sttdin.readline().rstrip('\n')]
        xor=0
        for i in range(1,len(nums)+1):
            xor^=(i^nums[i-1])
        sys.stdout.write(str(xor)+'\n')
'''