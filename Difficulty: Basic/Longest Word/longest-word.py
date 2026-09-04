class Solution:
    def longest(self, arr):
        max_len = 0
        longest_word = ""
        for i in range(len(arr)):
            if len(arr[i]) > max_len:
                max_len = len(arr[i])
                longest_word = arr[i]
        return longest_word
