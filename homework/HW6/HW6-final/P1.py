# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
    def _removemin(self, node):
        # find the most left child of node
        if node.left is None:
            return node.right
    
        else:
            node.left = self._removemin(node.left)
            node.size =  self._size(node.left) + self._size(node.right) + 1
            return node
    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        # TODO: Should return a subtree whose root is  but without
        #       the node whose key is 
            
        def find_min(node):
            #find min of the subtree
            while node.left:
                node = node.left
            return node
        
        if not node:
            raise KeyError('Error, key not in tree')
        
        if key < node.key:
            # if node.left:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            # if node.right:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None: 
                return node.right
            if node.right is None: 
                return node.left
            
            node_temp = node
            min_right = find_min(node.right)
            
            node = min_right
            node.right = self._removemin(node_temp.right)
            node.left = node_temp.left
            
            node.size = self._size(node.left) + self._size(node.right) + 1
            return node
        
class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        # TODO: implement
        self.tree = tree
        self.type = traversalType
        self.traverse = []
        self.index =0 
        
    def __iter__(self):
        # TODO: implement
        
        if self.type.value == 1:
            self.preorder(self.tree)
            
        elif self.type.value == 2:
            self.inorder(self.tree)
        
        else:
            self.postorder(self.tree)
        
        return self

    def __next__(self):
        try:
            tree = self.traverse[self.index]
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return tree
 
                
    def _inorder(self, node):
        if node.left:
            self._inorder(node.left)
            
        if node != None:
            self.traverse.append(node)
            
        if node.right:
            self._inorder(node.right)
            
    def _preorder(self, node):
        # TODO: implement
     
        if node != None:
            self.traverse.append(node)
            
        if node.left:
            self._preorder(node.left)
        
        if node.right:
            self._preorder(node.right)
    
    def _postorder(self, node):
        # TODO: implement
    
        if node.left:
            self._postorder(node.left)
            
        if node.right:
            self._postorder(node.right)
            
        if node != None:
            self.traverse.append(node)
            
    
    def inorder(self, bst: BSTTable):
        # TODO: implement
        self._inorder(bst._root)
       
    def preorder(self, bst: BSTTable):
        self._preorder(bst._root)
    
    def postorder(self, bst: BSTTable):
        self._postorder(bst._root)    

# demo
# if __name__ == "__main__":
#     print("<<<<<<<<<<<<<<<part A>>>>>>>>>>>>>>>")
#     t = BSTTable()
#     t.put(5, 'a')
#     t.put(1, 'b')
#     t.put(2, 'c')
#     t.put(0, 'd')
#     print(t._root)
#     print(t._root.size)
#     print(t._removemin(t._root))
#     print(t._root.size)
#     print("<<<<<<<<<<<<<<<part B>>>>>>>>>>>>>>>")
#     t = BSTTable()
#     t.put(5, 'a')
#     t.put(1, 'b')
#     t.put(2, 'c')
#     t.put(0, 'd')
#     print(t._remove(t._root, 5))
#     print(t._remove(t._remove(t._root, 5), 1))
#     #print(t._remove(t._root, 10))
#     print("<<<<<<<<<<<<<<<part C>>>>>>>>>>>>>>>")
#     input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
#     bst = BSTTable()
#     for key, val in input_array:
#         bst.put(key, val)
#     traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
#     for node in traversal:
#         print(str(node.key) + ', ' + node.val)