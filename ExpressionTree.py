#  File: ExpressionTree.py
#  Description: Traverse math operations using python trees
#  Student's Name: Weiyi Wang
#  Student's UT EID: ww6874
#  Course Name: CS 313E 
#  Unique Number: 87530
#
#  Date Created: 8/4/2016
#  Date Last Modified: 8/8/2016

class BinaryTree (object):

    def __init__ (self,initVal,parent):
        self.parent = parent
        self.data = initVal
        self.left = None
        self.right = None

    def createTree (self, expr):

        # Split the expressions into individual tokens
        tokenList = expr.split()
        
        current = self
        
        for token in tokenList:

            # Implement all the criteria for generating an infix tree
            
            # If the token is a ), the operation inside is completed
            if token == ')':
                current = current.parent

            # ( indicates start of a new operation, a new branch on the tree
            elif token == '(':

                # Insert a new BinaryTree as the left child
                # Move the current node down to the child
                # Set the parent of the new node as the original problem
                current.insertLeft(None)
                tempParent = current
                current = current.getLeftChild()
                current.parent = tempParent

            # If the token is an operator
            elif token in ['+','-','*','/']:

                # Change the data value to the operator
                # Insert a right child with parent as the existing tree
                # set the current node to the new node
                current.setRootVal(token)
                current.insertRight(self)
                tempParent = current
                current = current.getRightChild()
                current.parent = tempParent

            # If the token is an operand
            else:

                # Set the data of the current node to the eval(token)
                # Set the current node back to the parent
                current.data = eval(token)
                current = current.parent

            
               
    # Root is the top node of the subtree we want to evaluate
    def evaluate (self, root):

        # Base case is when you reach a leaf node, just return the number
        # Leaf nodes are signified by having no children
        if root.getLeftChild() == None and root.getRightChild() == None:
            return root.getRootVal()

        else:
            if root.getRootVal() == '+':
                return self.evaluate(root.getLeftChild()) + self.evaluate(root.getRightChild())

            elif root.getRootVal() == '-':
                return self.evaluate(root.getLeftChild()) - self.evaluate(root.getRightChild())

            elif root.getRootVal() == '*':
                return self.evaluate(root.getLeftChild()) * self.evaluate(root.getRightChild())
            
            elif root.getRootVal() == '/':
                return self.evaluate(root.getLeftChild()) / self.evaluate(root.getRightChild())
                       
    # prints a string of the expression in prefix form
    def preOrder (self, root):

        # Base case is when you reach a leaf node, just print the number
        # Leaf nodes are signified by having no children
        if root.getLeftChild() == None and root.getRightChild() == None:
            print(root.getRootVal(),end = ' ')

        else:

            print(root.getRootVal(), end = ' ')
            self.preOrder(root.getLeftChild())
            self.preOrder(root.getRightChild())


    def postOrder (self, root):
        # Base case is when you reach a leaf node, just print the number
        # Leaf nodes are signified by having no children
        if root.getLeftChild() == None and root.getRightChild() == None:
            print(root.getRootVal(),end = ' ')

        else:

            self.postOrder(root.getLeftChild())
            self.postOrder(root.getRightChild())
            print(root.getRootVal(), end = ' ')

    # Insert binary trees with no parent
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode,None)
        else:
            t = BinaryTree(newNode,None)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode,None)
        else:
            t = BinaryTree(newNode,None)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        self.data = value

    def getRootVal(self):
        return self.data

def main():

    in_file = open('treedata.txt','r')

    # Go through the lines, which are math expressions
    for line in in_file:

        # Create a new BinaryTree with no initial data and no initial parent
        exp = BinaryTree(None,None)

        print('Infix expression: ',line.rstrip())

        # Create the tree using the mathematic expression
        exp.createTree(line)

        print('Value: ',exp.evaluate(exp))

        print('Prefix expression:', end = ' ')
        exp.preOrder(exp)
        print()

        print('Postfix expression:', end = ' ')
        exp.postOrder(exp)
        print()
        print()
        
        

    

main()


