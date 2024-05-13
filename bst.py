class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while current:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if val > current.val:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right


    def search(self, val):
        return self.search_helper(self.root, val)

    def search_helper(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return node
        if val < node.val:
            return self.search_helper(node.left, val)
        return self.search_helper(node.right, val)

    
    def total_element(self):
        return self.size(self.root)

    def size(self , node):
        if node is None:
            return 0    
        count = 1
        count += self.size(node.left)
        count += self.size(node.right)
            
        return count
    

    def delete(self, val):
        self.root = self.delete_recursive(self.root, val)
    
    def delete_recursive(self, node, val):
        if node is None:
            return node
        
        if val < node.val:
            node.left = self.delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self.delete_recursive(node.right, val)
        else: 
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            node.val = successor.val
            
            if successor_parent != node:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        return node

# IN ORDER       
    def inorder_display(self):
        if self.root is None:
            print('Tree is Empty')
            return
        self.inorder_traversal(self.root)
        print()

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)

# PRE ORDER       
    def preOrder_display(self):
        if self.root is None:
            print('Tree is Empty')
            return
        self.preorder_traversal(self.root)
        print()

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

# POST ORDER       
    def postorder_display(self):
        if self.root is None:
            print('Tree is empty')
            return
        self.postorder_traversal(self.root)
    
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)  
            self.postorder_traversal(node.right)
            print(node.val, end=' ')

    
    

def main():

    obj = BST()

    obj.insert(25)
    obj.insert(10)
    obj.insert(7)
    obj.insert(26)
    obj.insert(18)
    obj.insert(9)
    obj.insert(45)
    obj.insert(30)
    obj.insert(1)
    obj.insert(40)
    print('In order')
    obj.inorder_display()
    print('Pre order')
    obj.preOrder_display()
    print('Post order')
    obj.postorder_display()
    print()
    print('Total Elements:' , obj.total_element())
    print('Element Deleted......') , obj.delete(7)
    print('Total Element After Deletion:' , obj.total_element())


main()

