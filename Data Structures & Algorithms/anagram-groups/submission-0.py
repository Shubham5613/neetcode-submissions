class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= []
        count = defaultdict(list)
        for s in strs:
            count[''.join(sorted(s))].append(s)
        for val in count.values():
            res.append(val)
        return res
        
        