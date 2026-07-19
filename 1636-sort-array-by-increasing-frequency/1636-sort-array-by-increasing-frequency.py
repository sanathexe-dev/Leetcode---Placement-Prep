class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        
        def custom(n):
            return (count[n],-n)
        
        nums.sort(key=custom)
        return nums
        