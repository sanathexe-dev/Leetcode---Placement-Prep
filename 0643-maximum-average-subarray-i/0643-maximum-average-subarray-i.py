class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur=0
        for i in range(k):
            cur+=nums[i]
        res=cur
        l=0
        for i in range(k,len(nums)):
            cur-=nums[l]
            cur+=nums[i]
            res=max(res,cur)
            l+=1
        return res/k

        