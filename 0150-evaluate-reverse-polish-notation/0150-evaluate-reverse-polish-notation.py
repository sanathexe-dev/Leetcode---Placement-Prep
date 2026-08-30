class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for c in tokens:
            if c=="+":
                stk.append(stk.pop()+stk.pop())
            elif c=="-":
                first=stk.pop()
                second=stk.pop()
                stk.append(second-first)
            elif c=="*":
                stk.append(stk.pop()*stk.pop())
            elif c=="/":
                first=stk.pop()
                second=stk.pop()
                stk.append(int(second/first))
            else:
                stk.append(int(c))
        return stk[-1]

        