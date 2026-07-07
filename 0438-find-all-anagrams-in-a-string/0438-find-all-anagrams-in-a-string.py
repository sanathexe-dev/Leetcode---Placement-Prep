class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window=[0]*26
        target=[0]*26
        
        for n in p:
            target[ord(n)-97]+=1
        lenp=len(p)
        l=0
        res=[]

        for r in range(len(s)):
            window[ord(s[r])-97]+=1

            if target==window:
                res.append(l)

            if lenp<=r-l+1:
                window[ord(s[l])-97]-=1
                l+=1
            
        return res



        