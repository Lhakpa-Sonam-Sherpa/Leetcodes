class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                j = nums.index(target-nums[i])
                if i != j:
                    return [min(i, j), max(i, j)]

sol = Solution()
# print(sol.twoSum([2,7,11,15], 9))
# print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))