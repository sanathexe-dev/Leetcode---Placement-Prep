class Solution:
    def trap(self, height: List[int]) -> int:



        l=0
        r=len(height)-1
        res=0
        MR=height[r]
        ML=height[l]
        while l<r:
            if ML<MR:
                l+=1
                ML=max(ML,height[l])
                res+=ML-height[l]
            else:
                r-=1
                MR=max(MR,height[r])
                res+=MR-height[r]
        return res

        