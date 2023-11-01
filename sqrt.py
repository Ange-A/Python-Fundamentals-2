# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.#
import math

class Solution(object):
    def mySqrt(self, x):
    
        sqrt_n = math.sqrt(x) 
        rounded = int(math.floor(sqrt_n))
        return rounded
    