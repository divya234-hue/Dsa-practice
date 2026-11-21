#minimum elemet find krte and usko starting position pr rkh dete

class Solution:
    def selectionSort(self,nums):
        n = len(nums)
        for i in range(n):#outer loop
            min_index = i
            for j in range(i+1,n):
                min_index = j
                if nums[j]<nums[j+1]:
                    nums[i],nums[min_index] = nums[min_index],nums[i]
        return nums