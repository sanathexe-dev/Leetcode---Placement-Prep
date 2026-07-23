class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        res=0
        for n in nums_set:
            if n-1 not in nums_set:
                cur=n
                large=1
                while (cur+1) in nums_set:
                    large+=1
                    cur+=1
                res=max(large,res)
        return res





        