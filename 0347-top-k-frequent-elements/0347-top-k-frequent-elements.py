class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for _ in range(len(nums)+1)]
        count={}
        res=[]
        for c in nums:
            count[c]=count.get(c,0)+1
        for n,c in count.items():
            freq[c].append(n)
        
        for c in range(len(freq)-1,-1,-1):
            for j in freq[c]:
                res.append(j)

                if len(res)==k:
                    return res 


        
                
            
        
        