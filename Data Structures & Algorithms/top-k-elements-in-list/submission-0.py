class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        count = Counter(nums)
        for key,val in count.items():
            heapq.heappush(h,(-val,key))
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res


        