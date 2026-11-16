class Solution:
    def twoSum(self,num,target):
        seen = {}
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]+num[j] == target:
                    return i,j
num = [2,3,4,5,8]
target = 5
obj = Solution()
print("two sum is:",obj.twoSum(num,target))