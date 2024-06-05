class Solution:
    def climbStairs(self, n: int) -> int:
        """
        재귀로 생각했으나 재귀함수는 function call이 너무많아져 time limit이 걸림
        
        동적(dynamic programming을 통해 배열과 반복문을 통해 앞전 내용을 기반으로 다음 결과를 구하는 형태로 구현)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        step1 = 1 
        step2 = 2
        
        for i in range(3, n + 1):
            current = step1 + step2
            step1 = step2
            step2 = current
        
        return step2