class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            com=target-nums[i]

            if com in h:
                return [i,h[com]]
            
            h[nums[i]]=i
        return 0
            
        
        

        
    