#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:35:10 2020

@author: Elliott
"""

# Node structure to create binary trees
class Node:

    # Define of nodes - data, left and right children    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Print data contained in a given node
    def print_node(self):
        print(self.data)

    # Return height of node (maximum level in tree)
    def height(self, level, max_level):
        
        level += 1
        if level > max_level:
            max_level = level
        
        if (self.left is not None):
            max_level = self.left.height(level, max_level)
            
        if (self.right is not None):
            max_level = self.right.height(level, max_level)
          
        return max_level

    # Return nodes in depth-first order - descend fully down each branch first
    def deep_list(self, level, lst):
        
        level += 1
        
        print("Level = ", level, "data = ", self.data)
        lst.append(self.data)
        
        if (self.left is not None):
            self.left.deep_list(level, lst)
            
        if (self.right is not None):
            self.right.deep_list(level, lst)
        
        return lst

    # Return nodes in breath-first order - each level at a time, left to right
    # Doesn't currently work
    def breadth_list(self, level, lst):
        
        level += 1
        
        print("Level = ", level, "data = ", self.data)
        lst.append(self.data)
        
        if (self.left is not None):
            self.left.breadth_list(level, lst)
            
        if (self.right is not None):
            self.right.breadth_list(level, lst)
        
        return lst        


# Create some nodes for tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 

#Print various nodes
# root.print_node() # Equivalent to print(root.data)
# root.left.print_node()
# root.right.print_node()
# root.left.left.print_node()
# root.left.right.print_node()

# Print whether nodes exist - useful expressions used
# print(root.right.right is None)
# print(root.left.right is None)

print("Deep list = ", root.deep_list(0, []))
print("Breadth list = ", root.breadth_list(0, []))
print("Tree height = ", root.height(0, 0))