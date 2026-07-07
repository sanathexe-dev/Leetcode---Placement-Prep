class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        res=""
        sum1=0
        for i in range(len(s)):
            if s[i]!="0":
                res+=s[i]
                sum1+=int(s[i])
        if res=="":
            return 0
        return int(res)*sum1
            



        