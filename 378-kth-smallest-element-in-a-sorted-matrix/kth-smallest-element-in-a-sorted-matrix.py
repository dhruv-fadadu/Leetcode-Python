class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(itertools.chain(*matrix))[k-1]