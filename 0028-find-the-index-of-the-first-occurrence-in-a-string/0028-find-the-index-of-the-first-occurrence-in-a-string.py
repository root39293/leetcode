class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            i = haystack.index(needle) #.index() 활용
        except ValueError:
            return -1
        return i
            
        
        