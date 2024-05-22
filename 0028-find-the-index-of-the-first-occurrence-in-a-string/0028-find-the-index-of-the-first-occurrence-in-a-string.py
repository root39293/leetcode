class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try: 
            i = haystack.index(needle) #.index() 활용
        except ValueError: # 문자열이 존재하지않을경우 ValueError 예외가 발생하므로 -1반환 
            return -1
        return i
            
        
        