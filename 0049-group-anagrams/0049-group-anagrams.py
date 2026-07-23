class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-97]+=1
            res[tuple(count)].append(i)
        return list(res.values())

        res=defaultdict(list)
        for c in strs:
            count=[0]*26
            for i in c:
                count[ord(i)-97]+=1
            res[tuple(count)].append(c)
        return list(res.values())





        