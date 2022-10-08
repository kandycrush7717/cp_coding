import sys
if __name__ == '__main__':
    nums = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
    target = int(sys.stdin.readline().rstrip('\n'))
    num_dict = {}
    n = len(nums)
    ans = []
    for i in range(n):
        compli = target-nums[i]
        if compli in num_dict:
            ans = [i, num_dict[compli]]
        num_dict[nums[i]] = i
    sys.stdout.write(str(ans))
