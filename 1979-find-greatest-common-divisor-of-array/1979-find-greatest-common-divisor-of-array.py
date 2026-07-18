class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        res=[]
        for i in range(1,mini+1):
            if mini%i==0 and maxi%i==0:
                res.append(i)
        return res[-1]

        