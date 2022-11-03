'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-03
    * Time : 7:46 p.m.
    * Question :(https://leetcode.com/problems/product-of-array-except-self/)
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
        the elements of nums except nums[i].
    * Example :
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
'''
import sys
# O(n) time and O(n) space
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        fp = [1]
        for i in nums:
            fp.append(fp[-1] * i)
        fp = fp[:-1]
        bp = [1]
        for i in nums[::-1]:
            bp.append(bp[-1] * i)
        bp = bp[:-1][::-1]
        ans = [fp[i] * bp[i] for i in range(len(fp))]
        print(ans)
#O(n) time and O(1) space
# ans=[1]
# for i in nums:
#     ans.append(ans[-1]*i)
# ans=ans[:-1]
# bp=1
# for i in range(-1,-1*len(ans)-1,-1):
#     ans[i]*=bp
#     bp*=nums[i]
# print(ans)
