class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in complement:
                return [i,complement[com]]
            complement[nums[i]]=i

        
        