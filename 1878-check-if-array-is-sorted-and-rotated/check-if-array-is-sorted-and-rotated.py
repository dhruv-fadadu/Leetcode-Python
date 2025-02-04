class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        last = nums[0]
        order_change = 0
        for i in range(1, n, 1):
            if last > nums[i]:
                order_change += 1
            last = nums[i]
        if (order_change == 1 and last<=nums[0]) or order_change == 0:
            return True
        return False