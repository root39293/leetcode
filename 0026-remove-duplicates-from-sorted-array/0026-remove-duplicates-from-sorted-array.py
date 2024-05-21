
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        q = sorted(set(nums)) #set은 본질적으로 순서가없지만 sorted 메소드로 정렬한 '리스트'를 리턴
        k = len(q)
        
        for i in range(k):
            nums[i] = q[i]

        return k
        
# sorted()는 내장 함수, sort()는 리스트의 메서드
# sorted()는 새로운 정렬된 리스트 반환, sort()는 해당 리스트 자체 정렬
# sorted()는 모든 이터러블에 사용 가능, sort()는 리스트에서만 사용 가능
# sorted()는 원본 리스트 변경 없음, sort()는 원본 리스트 자체 정렬