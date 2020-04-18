#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:35:10 2020

@author: Elliott
"""

# Trees
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)


root = Node(1)
# root.PrintTree()
root.left = Node(2)
# root.PrintTree()
root.right = Node(3)
# root.PrintTree()
root.left.left = Node(4)

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
