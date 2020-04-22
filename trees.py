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
    def height(self, level=0, max_level=0):
        
        level += 1
        if level > max_level:
            max_level = level
        
        if (self.left is not None):
            max_level = self.left.height(level, max_level)
            
        if (self.right is not None):
            max_level = self.right.height(level, max_level)
          
        return max_level


    # Return nodes in depth-first order - descend fully down each branch first
    def deep_list(self, level=0, lst=[]):
        
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
    # Want self, then self.left, self.right, then
    # self.left.left, self.left.right, self.right.left, self.right.right
    # etc...
    def breadth_list(self, current_level=0, max_level=1, lst=[], cont=False):

        # print(max_level)        

        current_level += 1

        if ((current_level == 1) and max_level == 1):
            lst.append(self.data)
            max_level += 1
        
        if (current_level < max_level):
            
            if (self.left is not None):
                lst, cont = self.left.breadth_list(current_level, max_level, lst, cont)
            
            if (self.right is not None):
                lst, cont = self.right.breadth_list(current_level, max_level, lst, cont)
        
            if (cont):
                max_level += 1
                self.breadth_list(max_level=max_level, lst=lst)
        
        if (current_level == max_level):

            lst.append(self.data)
            # print("Level = ", current_level, "data = ", self.data)

            if ((self.left is not None) or (self.right is not None)):
                # print("TEST")
                cont = True
        
        return lst, cont


# Create some nodes for tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 
root.right.left = Node(6)
root.right.right = Node(7)

#Print various nodes
# root.print_node() # Equivalent to print(root.data)
# root.left.print_node()
# root.right.print_node()
# root.left.left.print_node()
# root.left.right.print_node()

# Print whether nodes exist - useful expressions used
# print(root.right.right is None)
# print(root.left.right is None)

print("Deep list = ", root.deep_list())

lst, cont = root.breadth_list()
print("Breadth list = ", lst)

print("Tree height = ", root.height())