class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        sum,i=0,0
        for i in range (0,len(nums)+1):
            sum+=i
            print("sum=" , sum)
        nums_sum=0
        for n in nums:
            nums_sum+=n 
            print("nums_sum=" , nums_sum)

        return abs(nums_sum-sum)

