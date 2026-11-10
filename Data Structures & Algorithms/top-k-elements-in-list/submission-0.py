class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        return list(dict(sorted(d.items(), key=lambda kv: kv[1], reverse=True)).keys())[:k]