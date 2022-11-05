'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-05
    * Time : 12:28 a.m.
    * Question :(https://leetcode.com/problems/encode-and-decode-strings/)
        Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the
        network and is decoded back to the original list of strings.
    * Example :
        Input: dummy_input = ["Hello","World"]
        Output: ["Hello","World"]
        Explanation:
        Machine 1:
        Codec encoder = new Codec();
        String msg = encoder.encode(strs);
        Machine 1 ---msg---> Machine 2

        Machine 2:
        Codec decoder = new Codec();
        String[] strs = decoder.decode(msg);
'''
import sys
def encode(s):
    return ''.join(f'{len(x):3d}'+x for x in s)
def decode(e):
    d=[]
    i=0
    while(i<len(e)):
        l=int(e[i:i+3])
        i=i+3
        t=''
        for j in range(l):
            t+=e[j+i]
        i+=l
        d.append(t)
    return d
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=[x for x in sys.stdin.readline().rstrip('\n').split()]
        e=encode(s)
        d=decode(e)
        print(s)
        sys.stdout.write('encoded : '+e+'\n')
        print(d)
