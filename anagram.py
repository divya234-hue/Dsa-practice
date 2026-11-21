class Solution:
    def isanagram(self,s,t):
        if len(s)!= len(t):
            return False
        s = sorted(t)
        t = sorted(s)
        return s == t
obj = Solution()
print(obj.isanagram("cat","rat"))
print(obj.isanagram("nervous","previos"))