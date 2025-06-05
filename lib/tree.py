# class TreeNode:
#   """
#   1. Define node class: each node holds value and list of childs
#   """
#   def __init__(self, value):
#     self.value = value
#     self.children = []

class Tree:
  """
  2. add DFS to tree class
  """
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # inner function to recursively search
    def dfs(node):
      if node is None:
        return None
      
    # check if current node is the one we're looking for
      if node.get('id') == id:
        return node
      
    # recursively search children
      for child in node.get('children', []):
        found = dfs(child)
        if found: #if ID_match in subtree, return
          return found
      
      return None # No match in subtree too
  
    return dfs(self.root)
    
  
  
