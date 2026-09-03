class Solution:
    def twoSum(self, nums: list, target: int):
        value_map = {}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in value_map:
                return [value_map[remaining], i]

            else:
                value_map[nums[i]] = i


# TC - O(n)
# SC - O(n)