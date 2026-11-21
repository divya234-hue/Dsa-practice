class Solution:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        ans = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        while i < len(left):
            ans.append(left[i])
            i += 1

        while j < len(right):
            ans.append(right[j])
            j += 1

        return ans


obj = Solution()
arr = [5, 2, 8, 1, 3]
print(obj.mergeSort(arr))