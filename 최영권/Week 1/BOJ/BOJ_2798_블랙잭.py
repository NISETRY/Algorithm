# 블랙잭
N, M = map(int, input().split())

nums = list(map(int, input().split()))
three_num = set()
diff = []
for idx in range(len(nums)):
    three_num = set()
    for jdx in range(idx+1, len(nums)):
        three_num = set()
        for kdx in range(jdx+1, len(nums)):
            three_num = set()
            three_num.add(nums[idx])
            three_num.add(nums[jdx])
            three_num.add(nums[kdx])
            if sum(list(three_num)) <= M:
                diff.append(sum(list(three_num)))

print(sorted(diff)[-1])