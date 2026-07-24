class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                return mid
            
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1


        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r-=1
            else:
                l+=1
        return -1




        