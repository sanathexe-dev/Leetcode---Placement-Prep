class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1=[0]*26
        count2=[0]*26
        for i in t:
            count1[ord(i)-97]+=1
        for i in s:
            count2[ord(i)-97]+=1
        return count1==count2

        