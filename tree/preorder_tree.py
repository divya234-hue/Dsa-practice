class Solution:
    def preorder(self,root):
        result =[]
        def dfs(node):
            if node is None:
                return 
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        return (root)
        return result
