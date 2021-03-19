# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 未排序版普通完全树
# class Solution:
#     def sortedArrayToBST(nums) :
#         if not len(nums):
#             return
#         tree = TreeNode(nums[0])
#         stack = []
#         stack.append(tree)
#         for i in range(1,len(nums)):
#             data = nums[i]
#             while stack:
#                 insert = stack.pop(0)
#                 if insert.left == None:
#                     insert.left = TreeNode(data)
#                     stack.append(insert)
#                     break
#                 elif insert.right == None:
#                     insert.right = TreeNode(data)
#                     stack.append(insert)
#                     break
#                 else:
#                     stack.append(insert.left)
#                     stack.append(insert.right)
#         return tree
# class Solution:
#     def sortedArrayToBST(nums) :
#         l = int(len(nums)/2)
#         tree = TreeNode(nums[l])
#         for i in range(len(nums)):
#             if i == l:
#                 continue
#             data = TreeNode(nums[i])
#
#             def insert(data, tree):
#                 if data.val > tree.val:
#                     if tree.right == None:
#                         tree.right = data
#                     else:
#                         insert(data, tree.right)
#                 elif data.val < tree.val:
#                     if tree.left == None:
#                         tree.left = data
#                     else:
#                         insert(data, tree.left)
#             insert(data,tree)
#         return tree

class Solution:
    def sortedArrayToBST(nums) :
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[: mid])
        root.right = sortedArrayToBST(nums[mid + 1:])

        return root

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    mid = len(nums)//2
    print(nums[:mid])
    print(nums[mid+1:])
    print(Solution.sortedArrayToBST(nums))