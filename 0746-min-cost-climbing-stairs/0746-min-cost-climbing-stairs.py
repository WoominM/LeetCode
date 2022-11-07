class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # c1, c2 = 0, 0
        cost = [0, 0] + cost + [0]
        mincosts = [0, 0]
        for n in range(2, len(cost)):
            mincost = min(cost[n-1] + mincosts[n-1], cost[n-2] + mincosts[n-2])
            mincosts.append(mincost)
        return mincosts[-1]