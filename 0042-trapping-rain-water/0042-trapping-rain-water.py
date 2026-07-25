class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        ML=height[l]
        MR=height[r]
        while l<r:
            if MR>ML:
                l+=1
                ML=max(ML,height[l])
                res+=ML-height[l]
            else:
                r-=1
                MR=max(MR,height[r])
                res+=MR-height[r]
        return res


        