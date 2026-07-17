class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)<=2:
                return max(nums)

        def robmax(nums):
            n=len(nums)
            dp=[0]*n
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        return max(robmax(nums[1:]),robmax(nums[:-1]))
        
        