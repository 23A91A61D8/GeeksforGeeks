class Solution:
    def findMedian(self, arr):
        arr = sorted(arr)
        median = len(arr) // 2
        if len(arr) % 2 != 0:
            return arr[median]
        else:
            return (arr[median - 1] + arr[median]) / 2
