class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sort=set(nums)
        res=0
        for i in nums_sort:
            cur=i
            if cur-1 not in nums_sort:
                large=1
                while (cur+large) in nums_sort:
                    large+=1
                res=max(res,large)
        return res








        