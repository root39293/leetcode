class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        elif not strs:
            return ""
        else:
            shortest_string_length = len(min(strs, key=len))  
            prefix = ""
            
            for i in range(shortest_string_length):
                current_char = strs[0][i]
                for s in strs:
                    if s[i] != current_char:
                        return prefix  
                prefix += current_char
            
            return prefix  