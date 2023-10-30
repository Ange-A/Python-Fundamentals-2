class Solution(object):
    def Valid(self, s):
        k = len(s)
        for i in range(k):
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        
        if (len(s) == 0):
            return True
        else:
            return False
    
    