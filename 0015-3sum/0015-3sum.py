class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1

            while left<right:
                threesum=nums[i]+nums[left]+nums[right]
                if threesum>0:
                    right-=1
                elif threesum<0:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res


        nums.sort()
        res=[]
        for i in range(len(nums)):
            while i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1

            while left<right:
                threesum=nums[i]+nums[left]+nums[right]
                if threesum>0:
                    right-=1
                elif threesum<0:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res





        

                
        