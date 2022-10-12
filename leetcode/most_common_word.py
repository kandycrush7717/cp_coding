'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-11
    * Time : 10:43 p.m.
    * Question :(https://leetcode.com/problems/most-common-word/)
        Given a string paragraph and a string array of the banned words banned, return the most frequent word that
        is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

        The words in paragraph are case-insensitive and the answer should be returned in lowercase.
    * Example :
        Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
        Output: "ball"
        Explanation:
        "hit" occurs 3 times, but it is a banned word.
        "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
        Note that words in the paragraph are not case sensitive,
        that punctuation is ignored (even if adjacent to words, such as "ball,"),
        and that "hit" isn't the answer even though it occurs more because it is banned.

'''
import sys
import re
if __name__=='__main__':
    paragraph=sys.stdin.readline().rstrip('\n')
    banned=sys.stdin.readline().rstrip('\n').split(' ')
    word_count={}
    words=re.split('''\!|\?|\'| |\,|\;|\.|"''',paragraph)
    for i in words:
        if len(i)>0:
            if i in word_count:
                word_count[i]+=1
            else:
                word_count[i]=1
    sorted_word_count=dict(sorted(word_count.items(),key=lambda x:x[1],reverse=True))
    for i in sorted_word_count.keys():
        if i not in set(banned):
            sys.stdout.write(i+'\n')
            break