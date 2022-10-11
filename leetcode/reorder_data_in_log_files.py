'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-11
    * Time : 5:01 p.m.
    * Question :(https://leetcode.com/problems/reorder-data-in-log-files/)
        You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

        There are two types of logs:

        Letter-logs: All words (except the identifier) consist of lowercase English letters.
        Digit-logs: All words (except the identifier) consist of digits.
        Reorder these logs so that:

        The letter-logs come before all digit-logs.
        The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
        The digit-logs maintain their relative ordering.
        Return the final order of the logs.
    * Example :
        Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        Explanation:
        The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
        The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
'''
import sys

if __name__=='__main__':
    logs=[sys.stdin.readline().rstrip('\n').split(',')]
    word_logs=[]
    digit_logs=[]
    for i in logs:
        i_lst=i.split(' ')
        if i_lst[1].isdigit():
            digit_logs.append(i)
        else:
            word_logs.append(i)
    word_dict={}
    for i in word_logs:
        key=(i.split(' ',maxsplit=1))[1]
        if key in word_dict:
            word_dict[key].append(i)
        else:
            word_dict[key]=[i]
    ans=[]
    word_dict_keys=list(word_dict.keys())
    word_dict_keys.sort()
    for i in word_dict_keys:
        values=word_dict[i]
        if len(values)==1:
            ans.extend(values)
        else:
            values.sort()
            ans.extend(values)
    ans.extend(digit_logs)
    for i in ans:
        sys.stdout.write(i+' ')
    sys.stdout.write('\n')