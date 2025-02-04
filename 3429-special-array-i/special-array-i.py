class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        special = True
        for i in range(1, len(nums), 1):
            if nums[i-1] % 2 == nums[i] % 2:
                special = False
        return special