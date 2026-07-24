class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        temp=temperatures
        stk=[]
        res=[0]*len(temp)
        for i in range(len(temp)):
            while stk and temp[stk[-1]]<temp[i]:
                idx=stk.pop()
                res[idx]=i-idx
            stk.append(i)
        return res


                
        