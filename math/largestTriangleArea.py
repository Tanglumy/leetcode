class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2 for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))
