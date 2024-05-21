class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i], nums[n-1] = nums[n-1], nums[i] #자리바꾸기 ex) b,a = a,b
                n -= 1 # n과 i를 각각 -1, +1씩해 val이 등장한경우 마지막에서부터 차례대로 값을 교환
            else:
                i += 1 
        return k 