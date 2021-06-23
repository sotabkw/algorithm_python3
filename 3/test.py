n = 0
for i in range(1900000):
    if n > 15:
        print(i)
    else:
        n = 0

    for index in range(i):
        if i != 0:
            n += 1/i


def twoSum(self, nums: List[int], target: int) -> List[int]:
    value_dict = {}
    for i, num in enumerate(nums):
        remaining = target-num
        if remaining in value_dict:
            return [value_dict[remaining], i]
        value_dict[num] = i
    return []
