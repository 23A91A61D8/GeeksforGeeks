import math
class Solution:
    def lcmAndGcd(self, a, b):
        gcd_val = math.gcd(a, b)
        lcm_val = (a*b) // gcd_val
        return [lcm_val, gcd_val]
        