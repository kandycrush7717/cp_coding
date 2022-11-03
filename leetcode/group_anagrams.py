'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-03
    * Time : 1:46 p.m.
    * Question :(https://leetcode.com/problems/group-anagrams/)
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    * Example :
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        strs=[x for x in sys.stdin.readline().rstrip('\n').split()]
        ana_dict = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in ana_dict:
                ana_dict[temp].append(i)
            else:
                ana_dict[temp] = [i]
        print(list(ana_dict.values()))