class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        dict = {needle}
        
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] in dict:
                return i
        
        return -1
        