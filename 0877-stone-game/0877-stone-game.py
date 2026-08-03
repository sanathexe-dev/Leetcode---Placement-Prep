class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice=0
        bob=0
        l=0
        r=len(piles)-1
        c=0
        while l<r:
            c+=1
            if c%2!=0:
                if piles[l]>piles[r]:
                    alice+=piles[l]
                    l+=1
                else:
                    alice+=piles[r]
                    r-=1
            else:
                if piles[l]>piles[r]:
                    bob+=piles[r]
                    r-=1
                else:
                    bob+=piles[l]
                    l+=1
        return True if alice>bob else False
            
        