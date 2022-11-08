'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-08
    * Time : 4:09 p.m.
    * Question :(https://leetcode.com/problems/longest-repeating-character-replacement/)
        You are given a string s and an integer k. You can choose any character of the string and change it to any
        other uppercase English character. You can perform this operation at most k times.
        Return the length of the longest substring containing the same letter you can get after performing the above
        operations.
    * Example :
        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.
'''
import sys


def getMax(count_dict):
    maxi = 0
    for i in count_dict:
        maxi = max(maxi, count_dict[i])
    return maxi
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        k=int(sys.stdin.readline().rstrip('\n'))
        count_dict = {chr(x): 0 for x in range(65, 91)}
        i = 0
        j = 0
        max_len = 0
        while (i < len(s) and j < len(s)):
            count_dict[s[j]] += 1
            if (j - i + 1) - self.getMax(count_dict) <= k:
                max_len = max(j - i + 1, max_len)
            else:
                while ((j - i + 1) - self.getMax(count_dict) > k):
                    count_dict[s[i]] -= 1
                    i += 1
            j += 1
        sys.stdout.write(str(max_len)+'\n')
'''
            Optmized Version
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        k=int(sys.stdin.readline().rstrip('\n'))
        count_dict={chr(x):0 for x in range(65,91)}
        i=0
        j=0
        max_len=0
        while(i<len(s) and j<len(s)):
            count_dict[s[j]]+=1
            if (j-i+1)-self.getMax(count_dict)<=k:
                max_len=max(j-i+1,max_len)
            else:
                while((j-i+1)-self.getMax(count_dict)>k):
                    count_dict[s[i]]-=1
                    i+=1
            j+=1
        sys.stdout.write(str(max_len)+'\n')
        
'''