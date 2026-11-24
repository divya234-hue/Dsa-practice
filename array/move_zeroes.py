class Solution:
    def move(self,nums):
        nums = list(map(int, input("Enter array: ").split()))
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                  nums[i],nums[j] = nums[j],nums[i]
                  j = j+1