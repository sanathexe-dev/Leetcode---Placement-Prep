class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp=temperatures
        res=[0]*len(temp)
        stk=[]
        for i in range(len(temp)):
            while stk and temp[stk[-1]]<temp[i]:
                idx=stk.pop()
                res[idx]=i-idx
            stk.append(i)
        return res

                
        