class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq=[[] for _ in range(len(nums)+1)]
        count={}
        res=[]
        for c in nums:
            count[c]=1+count.get(c,0)
        for n,c in count.items():
            freq[c].append(n)
        for i in range(len(freq)-1,-1,-1):
            for c in freq[i]:
                res.append(c)
            if len(res)==k:
                return res


        
                
            
        
        