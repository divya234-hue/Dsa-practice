class Solution:
    def postorder(self,root):
        result =  []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            dfs.append(node.val)
        return (root)
        return result
    


