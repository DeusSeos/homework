from BinaryTree import BinaryTree

def main():
    tree = BinaryTree()
    tree.insert("200 Is it a shooter?")
    tree.insert("99 Can you destroy the environment?")
    tree.insert("48 ")


    printTree(tree)

def printTree(tree):
    # Traverse tree
    print("Inorder (sorted): ", end = "")
    tree.inorder()
    print("\nPostorder: ", end = "")
    tree.postorder()
    print("\nPreorder: ", end = "")
    tree.preorder()
    print("\nThe number of nodes is " + str(tree.getSize()))

main()
