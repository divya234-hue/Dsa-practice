class Solution:
    def bubble_sort(self,num):
        n = len(num)
        for i in range(num):
            for j in range(n-i-1):
                if num[j]>num[j+1]:
                    num[j],num[j+1] = num[j+1],num[j]
        return num

