class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        cto={"}":"{","]":"[",")":"("}
        for i in s:
            if i in cto:
                if stk and cto[i]==stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return not stk
