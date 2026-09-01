class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter={0:1}
        for n in nums:
            temp={}

            for t,c in counter.items():
                temp[t+n]=temp.get(t+n,0)+c
                temp[t-n]=temp.get(t-n,0)+c
            counter=temp

        return counter.get(target,0)
        