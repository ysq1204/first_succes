# 1. BinaryTree (二叉树)

# 二叉树是有限个元素的集合，该集合或者为空、或者有一个称为根节点（root）的元素及两个互不相交的、分别被称为左子树和右子树的二叉树组成。

# 二叉树的每个结点至多只有二棵子树(不存在度大于2的结点)，二叉树的子树有左右之分，次序不能颠倒。
# 二叉树的第i层至多有2^{i-1}个结点
# 深度为k的二叉树至多有2^k-1个结点；
# 对任何一棵二叉树T，如果其终端结点数为N0，度为2的结点数为N2，则N0=N2+1

# 1.生成二叉树

#
# def init_binary_tree(data, lenght):
#     root = BTNode(data[0])
#
#     for x in range(1, lenght):
#         node = BTNode(data[x])
#         InsertElementBinaryTree(root, node)
#     return root
#     print('done')


# -*- coding: utf-8 -*-

"""
Created on Mon Apr 03 19:58:58 2017

@author: Administrator
"""


class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 深度
def depth(tree):
    if tree == None:
        return 0
    left, right = depth(tree.left), depth(tree.right)
    return max(left, right) + 1


# 前序遍历
def pre_order(tree):
    if tree == None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)


# 中序遍历
def mid_order(tree):
    if tree == None:
        return
    mid_order(tree.left)
    print(tree.data)
    mid_order(tree.right)


# 后序遍历
def post_order(tree):
    if tree == None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)


# 层次遍历
def level_order(tree):
    if tree == None:
        return
    q = []
    q.append(tree)
    while q:
        current = q.pop(0)
        print(current.data)
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)


# 按层次打印
def level2_order(tree):
    if tree == None:
        return
    q = []
    q.append(tree)
    results = {}
    level = 0
    current_level_num = 1
    nextlevelnum = 0
    d = []
    while q:
        current = q.pop(0)
        current_level_num -= 1
        d.append(current.data)
        if current.left != None:
            q.append(current.left)
            nextlevelnum += 1
        if current.right != None:
            q.append(current.right)
            nextlevelnum += 1
        if current_level_num == 0:
            current_level_num = nextlevelnum
            nextlevelnum = 0
            results[level] = d
            d = []
            level += 1
    print(results)


if __name__ == '__main__':
    tree = node('D', node('B', node('A'), node('C')), node('E', right=node('G', node('F'))))
    print('前序遍历：')
    pre_order(tree)
    print('\n')
    print('中序遍历：')
    mid_order(tree)
    print('\n')
    print('后序遍历：')
    post_order(tree)
    print('\n')
    print("层次遍历")
    level2_order(tree)

