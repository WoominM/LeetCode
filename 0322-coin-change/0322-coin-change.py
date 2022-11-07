class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        array = [-1] * (amount + 1)
        array[0] = 0
        for n in range(1, amount+1):
            for i in coins:
                if n-i >= 0 and array[n-i] != -1:
                    if array[n] == -1:
                        array[n] = float('inf')
                    array[n] = min(array[n-i], array[n])
                # print(n, i, n-i, array)
            if array[n] != -1:
                array[n] += 1
        return array[-1] if array[-1] != -1 else -1