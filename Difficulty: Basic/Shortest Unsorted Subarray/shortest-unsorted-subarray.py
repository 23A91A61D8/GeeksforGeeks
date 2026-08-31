class Solution:
    def shortestUnorderedSubarray(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        for i in range(n - 2):
            a = arr[i]
            b = arr[i + 1]
            c = arr[i + 2]
            if (a < b and b > c) or (a > b and b < c):
                return 3
        return 0
