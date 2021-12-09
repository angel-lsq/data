# # import pandas as pd
# # import numpy as np
# # # s = pd.Series(np.random.randn(233))
# # s = np.random.randn(233)
# # print(s.size)
#
# #先定义一颗二叉树
# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def get(self):
#         return self.data
#
#     def getLeft(self):
#         return self.left
#
#     def getRight(self):
#         return self.right
#
#     def setLeft(self, node):
#         self.left = node
#
#     def setRight(self, node):
#         self.right = node
#
# #实例化一颗二叉树..为一颗满二叉树
# binaryTree = BinaryTree(0)  #根
# binaryTree.setLeft(BinaryTree(1))  #第二层的左序列
# binaryTree.setRight(BinaryTree(2))   #第二层的右序列
# binaryTree.getLeft().setLeft(BinaryTree(3))  #第三层的左序列的左
# binaryTree.getLeft().setRight(BinaryTree(4))  #第三层的左序列的右
# binaryTree.getRight().setLeft(BinaryTree(5))   #第三层的右序列的左
# binaryTree.getRight().setRight(BinaryTree(6))   #第三层的右序列的右
#
# #前序
# def preorderTraversal(now, result=[]):
#     if now == None:
#         return result
#     result.append(now.data)
#     preorderTraversal(now.left, result)
#     preorderTraversal(now.right, result)
#     return result
#
#
# print(preorderTraversal(binaryTree))
#
# #中序遍历
# def intermediateTraversal(now, result=[]):
#     if now == None:
#         return result
#     intermediateTraversal(now.left, result)
#     result.append(now.data)
#     intermediateTraversal(now.right, result)
#     return result
# print(intermediateTraversal(binaryTree))
#
#
# #后序
# def postorderTraversal(now, result=[]):
#     if now == None:
#         return
#     postorderTraversal(now.left, result)
#     postorderTraversal(now.right, result)
#     result.append(now.data)
#     return result
#
# print(postorderTraversal(binaryTree))
def func():
    try:
        print(1)
        i=100/0
        print(2)
        return
    except Exception as e:
        print(3)
    finally:
        print(4)
    print(5)
func()
