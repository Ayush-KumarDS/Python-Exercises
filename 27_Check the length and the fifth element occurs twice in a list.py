# Check the length and the fifth element occurs twice in a list

def test(nums):
    return len(nums) == 5 and nums.count(nums[4]) == 2

nums = [1,3,4,9,6,8,6,2,4,5,6,7,8,9,10,11,12,13,14,15]
nums2 = [2,5,8,5,6,6,6,8,3]
nums3 = [11, 12, 14, 13, 14, 13, 15, 14]


print(test(nums))
print(test(nums2))
print(test(nums3))