class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        i = 0
        
        while i < len(s):
            current_value = roman[s[i]]
            
            if i + 1 < len(s):
                next_value = roman[s[i + 1]]
                if current_value < next_value:
                    res += (next_value - current_value)
                    i += 2  
                else:
                    res += current_value
                    i += 1
            else:
                res += current_value
                i += 1
        
        return res