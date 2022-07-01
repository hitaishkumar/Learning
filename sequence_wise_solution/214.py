class treenode:
    def __init__(self,val = 0,right = None , left = None):
        self.val = val
        self.right = right
        self.left = left
        
def insertintobst(root: treenode , val : int ) -> treenode:
    if not root:
        return treenode(val)
    elif val > root.val:
        insertintobst(root.right , val)
    else:
        insertintobst(root.left, val)
    return root
