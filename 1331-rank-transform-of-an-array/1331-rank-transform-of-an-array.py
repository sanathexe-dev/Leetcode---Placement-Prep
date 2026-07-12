class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        nums1=sorted(arr)
        r=1
        for i in nums1:
            if i not in rank:
                rank[i]=r
                r+=1
        
        res=[]
        for i in arr:
            val=rank[i]
            res.append(val)
        return res     