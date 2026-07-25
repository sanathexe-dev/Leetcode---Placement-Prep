class Solution:
    def isHappy(self, n: int) -> bool:

        def check(n):
            s=0
            while n!=0:
                d=n%10
                s+=d**2
                n//=10
            return s
        
        h=set()
        while n!=1:
            n=check(n)
            if n in h:
                return False
            h.add(n)
        return True
            
        