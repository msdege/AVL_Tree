# bug-free-couscous
Python Implementation of Balanced Binary Search Tree (AVL Tree)

Contains methods to return height of the tree, insert and remove elements recursively, 
and retrieve a list representation as well as an in-order, post-order, and pre-order representation of the tree recursively.

Maintains height value by updating the height attribute of each node at each step in the recursive insertion and removal methods.

Balances the tree using private balance method which utilizes the heights to account for an imbalance in the tree and fix it.
This allows for, on average, O(logn) insertion and removal time. 
