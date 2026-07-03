class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        ML=height[left]
        MR=height[right]
        res=0

        while left<right:
            if ML<MR:
                left+=1
                ML=max(ML,height[left])
                res+=ML-height[left]
            else:
                right-=1
                MR=max(MR,height[right])
                res+=MR-height[right]
        return res

        