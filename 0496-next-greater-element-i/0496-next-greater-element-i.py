class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


 

        numsidx={n:i for i,n in enumerate(nums1)}
        stk=[]
        res=[-1]*len(nums1)
        for i in range(len(nums2)):
            while stk and stk[-1]<nums2[i]:
                val=stk.pop()
                idx=numsidx[val]
                res[idx]=nums2[i]
            if nums2[i] in numsidx:
                stk.append(nums2[i])
        return res


