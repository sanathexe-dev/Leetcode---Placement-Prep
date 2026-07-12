class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        target=[0]*26
        window=[0]*26

        for i in p:
            target[ord(i)-97]+=1
        lenp=len(p)
        res=[]
        l=0
        for r in range(len(s)):
            window[ord(s[r])-97]+=1

            if window==target:
                res.append(l)

            if (r-l+1)>=lenp:
                window[ord(s[l])-97]-=1
                l+=1
        return res

















        