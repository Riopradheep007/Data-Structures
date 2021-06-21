#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:07:00 2021

@author: pradheep
"""


'''
search complexity 
   bescase  O(log n)
   worst case O(n)
insert complixity
   best case  O(log n)
   worst case O(n)
Delete complixity
   best case  O(log n)
   worst case O(n)
space complixity 
   best case  O(n)
   worst case O(n)
'''
class Binary_Search_Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_child(self,data):
         #add small aa to the left
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_Search_Tree(data)

         #add data to the right
        else:       
            if data>self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right=Binary_Search_Tree(data)
                    
    def inorder_traversal(self):
        elements=[]
        
        if self.left:
            elements+=self.left.inorder_traversal()
        elements.append(self.data)
        print("elements added to the list",elements)
        
        if self.right:
            elements+=self.right.inorder_traversal()
        print(elements)
        return elements
    
    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            """ this line is every time recursive call new list is create
                checking the condition return the before node add the value"""
            elements+=self.left.pre_order_traversal()  
            
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def min_node(self):
        if self.left==None:
            return self.data
        return self.left.min_node()
    
    def max_node(self):
        if self.right==None:
            return self.data
        return self.right.min_node()
    
    def search_element(self,data):
        if data==self.data:
            return "element {} found".format(data)
        if data<self.data:
            if self.left:
                return self.left.search_element(data)
            else:
                return False
        if data>self.data:
            if self.right:
                return self.right.search_element(data)
            else:
                return False
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
    
def build_tree(elements):
    root=Binary_Search_Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
            
        
if __name__ =="__main__":
    elements=[17, 4, 1, 20, 9, 23, 18, 34]

    tree=build_tree(elements)
    print("inorder traverssal",tree.inorder_traversal())
    print("preorder traversal",tree.pre_order_traversal())
    print("post order traversal",tree.post_order_traversal())
    print("minimum elements",tree.min_node())
    print("maximum elemennts",tree.max_node())
    print("calculate sum",tree.calculate_sum())
    print("search element",tree.search_element(9))
    print("Delete",tree.delete(9))
    print("inorder traverssal",tree.inorder_traversal())
