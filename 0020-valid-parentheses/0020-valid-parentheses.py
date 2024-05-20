class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: # 길이가 홀수면 애초에 수식오류
            return False
        else:
            braket_dict = {")":"(","]":"[","}":"{",}
            stack = []
            for char in s:
                if char in braket_dict: # 만약 괄호 딕셔너리에 문자가 존재한다면(닫힌 괄호가 있다면)
                    if stack and stack[-1] == braket_dict[char]: # 스택의 마지막요소(가장 바깥에 열린 괄호)와 현재 문자열의 딕셔너리 벨류값과 같은가?
                        stack.pop() # 마지막요소 꺼내기
                    else:
                        return False
                else:
                    stack.append(char)

            return not stack # 스택이 모두 pop 될경우 빈리스트 반환함 not을 이용해 True