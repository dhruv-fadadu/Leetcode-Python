class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = suma = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >nums[i-1]:
                suma += nums[i]
            else:
                suma = nums[i]
            ans = max(suma, ans)
        return ans