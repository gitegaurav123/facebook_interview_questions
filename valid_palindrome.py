class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        
        start = 0
        end = len(s) -1
        while(start<end):
            if s[start].isalpha() == False  and s[start].isdigit() == False:
                print s[start], 'Not alpha'
                start += 1
                continue
            
            if s[end].isalpha() == False and s[end].isdigit() == False:
                print s[end], 'Not alpha'
                end -= 1
                continue
            
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True