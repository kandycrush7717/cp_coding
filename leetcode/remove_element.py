'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-03
    * Time : 4:14 p.m.
    * Question :(https://leetcode.com/problems/remove-element/)
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative
        order of the elements may be changed.
        Since it is impossible to change the length of the array in some languages, you must instead have the result
        be placed in the first part of the array nums. More formally, if there are k elements after removing the
        duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave
        beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array. You must do this by modifying the input array in-place with
        O(1) extra memory.
    * Example :
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
        It does not matter what you leave beyond the returned k (hence they are underscores).
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        val=int(sys.stdin.readline().rstrip('\n').split())
        i = 0
        j = len(nums) - 1
        while (i <= j):
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
            if i <= j:
                nums[i] = nums[j]
                i += 1
                j -= 1
        ans=max(i, j)
        sys.stdout.write(str(ans)+'\n')

# Other approach
# c=0
# for i in range(0,len(nums)):
#     if(nums[i]!=val):
#         nums[c]=nums[i]
#         c=c+1