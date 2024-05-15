class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        
        intToStr = str(x)
        length = len(intToStr)
        mid = length//2

        for i in range(mid):
            if intToStr[i] != intToStr[length - 1 - i]:
                return False
        return True