class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        cur=0
        res=float('inf')
        for r in range(len(nums)):
            cur+=nums[r]
            while cur>=target:
                res=min(res,r-l+1)
                cur-=nums[l]
                l+=1
        if res!=float('inf'):
            return res
        else:
            return 0


        