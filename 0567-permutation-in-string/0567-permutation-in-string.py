class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=[0]*26
        target=[0]*26
        lens1=len(s1)
        for i in s1:
            target[ord(i)-97]+=1
        l=0
        for r in range(len(s2)):
            window[ord(s2[r])-97]+=1

            if window==target:
                return True
            if lens1<=r-l+1:
                window[ord(s2[l])-97]-=1
                l+=1
        return False


