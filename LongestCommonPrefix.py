class Solution(object):
    def longestCommonPrefix(self, strs):
        longer = ""
        count = 0
        
        for i in strs:
            if len(i) < len(longer) or longer == "":
                longer = i
                
        required = len(strs)
        result = ''
        
                
        while required != count: 
            count = 0
            
            for i in strs:
                if longer == i[:len(longer)]:
                    count += 1
                
                result = longer
                longer = longer [:-1]
                
                if count == required:
                    return result
                else:
                    return ""