class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        return x_str == x_str[::-1]
        
        
pal = Solution()

result = pal.isPalindrome(121)
print (result)