'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-08
    * Time : 1:34 p.m.
    * Question :(https://leetcode.com/problems/longest-substring-without-repeating-characters/)
        Given a string s, find the length of the longest substring without repeating characters.
    * Example :
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        i = 0
        j = 0
        seenSet = set()
        max_len = 0
        if len(s) == 0:
            max_len=0
        else:
            while (i < len(s) and j < len(s)):
                if s[j] not in seenSet:
                    max_len = max(max_len, j - i + 1)
                    seenSet.add(s[j])
                    j += 1
                else:
                    while (s[j] in seenSet):
                        seenSet.remove(s[i])
                        i += 1
        sys.stdout.write(str(max_len)+'\n')
