class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res=float("-inf")
        cur=0
        for i in range(len(nums)):
            cur+=nums[i]
            res=max(res,cur)
            if cur<0:
                cur=0
        return res
        