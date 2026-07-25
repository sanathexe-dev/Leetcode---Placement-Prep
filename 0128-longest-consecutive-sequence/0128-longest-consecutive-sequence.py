class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        res=0
        for i in nums_set:
            cur=i
            if cur-1 not in nums_set:
                large=1
                while cur+1 in nums_set:
                    cur+=1
                    large+=1
                res=max(res,large)
        return res






        