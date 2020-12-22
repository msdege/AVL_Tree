class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.right_child = None
      self.left_child = None
      self.height = 1

  def __init__(self):
    self.__root = None

  def __return_height(self, root):
    if root.left_child is None and root.right_child is None:
      root.height=1                     #need special cases to account
    elif root.left_child is None:       #for when children are None
      root.height=root.right_child.height+1
    elif root.right_child is None:
      root.height=root.left_child.height+1
    else:
      root.height=max(root.left_child.height,root.right_child.height)+1
    return root.height

  def __balance(self, t):    #t is root of subtree
    if t is None:     #tree is already balanced
      print('t is none was executed')
      return t
    #when children are None, set height to 0. otherwise, self.height
    if t.right_child is None:
      right_child_height=0
    else:
      right_child_height=t.right_child.height
    if t.left_child is None:
      left_child_height=0
    else:
      left_child_height=t.left_child.height
    #rotations
    if (right_child_height-left_child_height)==-2:   #left-heavy
      #when subchildren are None, set height to 0
      if t.left_child.right_child is None:
        small_rchild_height=0
      else:
        small_rchild_height=t.left_child.right_child.height
      if t.left_child.left_child is None:
        small_lchild_height=0
      else:
        small_lchild_height=t.left_child.left_child.height
      if (small_rchild_height-small_lchild_height)==1:
        #left child is right-heavy, double rotation
                      #first rotation
        small_floater=t.left_child.right_child.left_child
        small_new_root=t.left_child.right_child
        small_old_root=t.left_child
        t.left_child=small_new_root
        small_old_root.right_child=small_floater
        small_new_root.left_child=small_old_root
        #recompute heights of small_new_root and small_old_root
        small_old_root.height=self.__return_height(small_old_root)
        small_new_root.height=self.__return_height(small_new_root)
                      #second rotation
        floater=t.left_child.right_child
        old_root=t
        t=small_new_root
        old_root.left_child=floater
        small_new_root.right_child=old_root
        #before returning, recompute height of two nodes, t and old root
        old_root.height=self.__return_height(old_root)
        t.height=self.__return_height(t)
        return t
      else:
        #left child is balanced or left-heavy, single rotation
        floater=t.left_child.right_child
        new_root=t.left_child
        old_root=t
        t=new_root
        old_root.left_child=floater
        new_root.right_child=old_root
        #before returning, recompute height of two nodes, t and old root
        old_root.height=self.__return_height(old_root)
        t.height=self.__return_height(t)
        return t
    elif (right_child_height-left_child_height)==2: #right_heavy
      #when subchildren are None, set height to 0
      if t.right_child.left_child is None:
        small_lchild_height=0
      else:
        small_lchild_height=t.right_child.left_child.height
      if t.right_child.right_child is None:
        small_rchild_height=0
      else:
        small_rchild_height=t.right_child.right_child.height
      if (small_rchild_height-small_lchild_height)==-1:
        #right child is left-heavy, double rotation
                        #first rotation
        small_floater=t.right_child.left_child.right_child
        small_new_root=t.right_child.left_child
        small_old_root=t.right_child
        t.right_child=small_new_root
        small_old_root.left_child=small_floater
        small_new_root.right_child=small_old_root
        #recompute heights of small_new_root and small_old_root
        small_old_root.height=self.__return_height(small_old_root)
        small_new_root.height=self.__return_height(small_new_root)
                        #second rotation
        floater=t.right_child.left_child
        old_root=t
        t=small_new_root
        old_root.right_child=floater
        small_new_root.left_child=old_root
        #before returning, recompute height of two nodes, t and old root
        old_root.height=self.__return_height(old_root)
        t.height=self.__return_height(t)
        return t
      else:
        #right child is balanced or right-heavy, single rotation
        floater=t.right_child.left_child
        new_root=t.right_child
        old_root=t
        t=t.right_child
        old_root.right_child=floater
        new_root.left_child=old_root
        #before returning, recompute height of two nodes, t and old root
        old_root.height=self.__return_height(old_root)
        t.height=self.__return_height(t)
        return t
    else:     #t is right-heavy or left-heavy by 1, or balanced. no rotation.
      return t

  def insert_element(self, value):
    self.__root=self.__recursive_insert(value,self.__root)

  def __recursive_insert(self, value, root):
    #base case
    if root==None:
      return self.__BST_Node(value)
    #recursive case
    if value<root.value:
      root.left_child=self.__recursive_insert(value,root.left_child)
    elif value>root.value:
      root.right_child=self.__recursive_insert(value,root.right_child)
    elif value==root.value:
      raise ValueError
    #update height of root before returning
    root.height=self.__return_height(root)
    return self.__balance(root)


  def remove_element(self, value):
    self.__root=self.__recursive_removal(value, self.__root)

  def __recursive_removal(self, value, root):
    if root==None:                    #value is not in tree
      raise ValueError
    #base case
    if value==root.value:                #found value to remove
      #root has zero children
      if root.left_child is None and root.right_child is None:
        return None                        
      #root has one child
      elif root.left_child is None or root.right_child is None:
        if root.left_child is not None:
          return root.left_child              
        elif root.right_child is not None:
          return root.right_child
      #root has two children
      elif root.left_child is not None and root.right_child is not None:
        t=root.right_child                   
        while t.left_child is not None:   #loop through to minimum on right
          t=t.left_child                  
        root.value=t.value          #copy value into root
        #recur again to remove duplicate
        root.right_child=self.__recursive_removal(t.value,root.right_child)
    #recursive case
    elif value<root.value:     #val is less than root's val, recur left 
      root.left_child=self.__recursive_removal(value,root.left_child)
    elif value>root.value:     #val is greater than root's val, recur right
      root.right_child=self.__recursive_removal(value,root.right_child)
    #update height of root before returning
    root.height=self.__return_height(root)
    return self.__balance(root)

  def to_list(self):    #return list of tree
    if self.__root==None:
      return []
    tree_list=self.__recursive_to_list(self.__root)
    return tree_list
    
  def __recursive_to_list(self, root):  
    #base case
    if root==None:
      return []
    #recursive case (Left, Parent, Right)((just like in_order traversal))
    tree_list=self.__recursive_to_list(root.left_child)+[root.value]+ \
      self.__recursive_to_list(root.right_child)
    return tree_list

  def in_order(self):        #create string representation of tree (LPR)
    if self.__root==None:
      return "[ ]"
    traversal=self.__recursive_in_order(self.__root)
    return ('[ '+traversal)[:-2]+' ]'

  def __recursive_in_order(self, root):
    #base case
    if root==None:
      return ''
    #recursive case (Left, Parent, Right)
    string=str(self.__recursive_in_order(root.left_child))\
      +str(root.value)+', '+str(self.__recursive_in_order(root.right_child))
    return string

  def pre_order(self):       #create string representation of tree (PLR)
    if self.__root==None:
      return "[ ]"
    traversal=self.__recursive_pre_order(self.__root)
    return ('[ '+traversal)[:-2]+' ]'
  
  def __recursive_pre_order(self, root):
    #base case
    if root==None:
      return ''
    #recursive case (Parent, Left, Right)
    string=str(root.value)+', '+\
      str(self.__recursive_pre_order(root.left_child))\
        +str(self.__recursive_pre_order(root.right_child))
    return string

  def post_order(self):      #create string representation of tree (LRP)
    if self.__root==None:
      return "[ ]"
    traversal=self.__recursive_post_order(self.__root)
    return ('[ '+traversal)[:-2]+' ]'
  
  def __recursive_post_order(self, root):
    #base case
    if root==None:
      return ''
    #recursive case (Left, Right, Parent)
    string=str(self.__recursive_post_order(root.left_child))+\
      str(self.__recursive_post_order(root.right_child))+str(root.value)+', '
    return string

  def get_height(self):
    if self.__root==None:   #special case
      return 0             
    else:
      return self.__root.height  #return height updated height attribute

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.

