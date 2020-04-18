# Given an integer n, generate all structurally unique BSTs that store values 1...n

def generateTrees(n: int) -> List[TreeNode]:
    def generate_util(root: TreeNode, nums: List[int], res: List[TreeNode]) -> List[TreeNode]:
        for i, n in enumerate(nums):
            node = TreeNode(n)
            if n < root.node:
                root.left = node
                generate_util(node, nums[:i] + nums[i + 1:], res)
            else:
                root.right = node
                generate_util(node, nums[:i] + nums[i + 1:], res)
