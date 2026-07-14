class Solution:
    def isNumber(self, s: str) -> bool:
        if "nan" in s or "inf" in s or "Infinity" in s:
            return False
        try:
            float(s)
            return True
        except:
            return False
        