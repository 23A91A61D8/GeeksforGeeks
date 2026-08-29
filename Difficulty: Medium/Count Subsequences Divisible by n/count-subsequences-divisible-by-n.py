class Solution:
    def countSubsequences(self, s: str, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n  
        for ch in s:
            digit = int(ch)
            new_dp = dp[:]  
            new_dp[digit % n] = (new_dp[digit % n] + 1) % MOD
            for r in range(n):
                if dp[r] > 0:
                    new_r = (r * 10 + digit) % n
                    new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD
            dp = new_dp
        return dp[0] 
