'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-03
    * Time : 4:34 p.m.
    * Question :(https://leetcode.com/problems/top-k-frequent-elements/)
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.
    * Example :
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        nums=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        k=int(sys.stdin.readline().rstrip('\n'))
        ans = []
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
        sorted_keys = list(sorted_dict.keys())
        min_len = min(len(sorted_keys), k)
        print(sorted_keys[:min_len])
