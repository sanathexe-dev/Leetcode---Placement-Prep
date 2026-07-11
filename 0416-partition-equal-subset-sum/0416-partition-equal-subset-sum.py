class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)

        for i in range(len(nums)):
            nextdp=set()
            for t in dp:
                nextdp.add(nums[i]+t)
                nextdp.add(t)
            dp=nextdp
        return True if target in dp else False

        