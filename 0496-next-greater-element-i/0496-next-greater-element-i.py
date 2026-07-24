class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        numsidx={n:i for i,n in enumerate(nums1)}
        stk=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stk and stk[-1]<cur:
                val=stk.pop()
                idx=numsidx[val]
                res[idx]=cur
            if cur in numsidx:
                stk.append(cur)
        return res