class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threesum=nums[l]+nums[r]+nums[i]
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res



        

                
        