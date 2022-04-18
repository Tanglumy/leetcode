class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        minTime = []
        maxtime = 24*60
        for i in range(n):
            x, y = timePoints[i].split(":")
            minTime.append(int(x)*60+int(y))
        minTime = sorted(minTime)
        result = 24*60
        for i in range(len(minTime)-1):
            result = min(result, maxtime -
                         minTime[i+1]+minTime[i], minTime[i+1]-minTime[i])
        result = min(result, maxtime-minTime[-1]+minTime[0])
        print(result)
        return result
