class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cur=0
        res=max(nums)
        for i in range(len(nums)):
            cur+=nums[i]
            res=max(res,cur)
            if cur<0:
                cur=0
        return res
        