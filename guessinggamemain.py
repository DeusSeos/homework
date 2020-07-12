from BinaryTree import BinaryTree

def displayMenu():
    options = ["P Play the game", "L Load another game file", "D Display the binary tree",
               "H Help information", "X Exit the program"]
    print()
    for choice in options:
        print(choice)
    print()

def orderMenu():
    print("\nIn what order do you want to display?")
    print("In   Inorder")
    print("Pre  Preorder")
    print("Post Postorder")
    print("R Return to main menu")

def helpMenu():
    print()

def orderChoice(tree):
    orderMenu()
    choice = input("Enter in a display order choice: ")
    listChoice = ["pre", 'post', "in", "return"]
    while choice not in listChoice:
        print("\nEnter a valid choice from the menu.")
        orderMenu()
        choice = input("Enter in your choice: ").strip().lower()
    if choice == 'pre':
        tree.preorder()
    elif choice == 'post':
        tree.postorder()
    elif choice == 'in':
        tree.inorder()
    else:
        return

def displayChoice():
    displayMenu()
    listChoice = ['p', 'l', 'd', 'h', 'x']
    choice = input("Enter in your choice: ").strip().lower()
    while choice not in listChoice:
        print("\nEnter a valid choice from the menu.")
        displayMenu()
        choice = input("Enter in your choice: ").strip().lower()
    return choice

def runFuntion(choice, tree):
    if choice == 'p':
        fileLoading(filename="Game1.txt", tree = tree)
    elif choice == 'l':
        newFile = input("Enter in the game file you want to load: ").strip()
        fileLoading(newFile, tree)
    elif choice == 'd':
        orderChoice(tree)
    elif choice == 'h':
        helpMenu()
    else:
        return



def fileLoading(filename, tree):
    filename = filename
    try:
        with open(filename, 'r') as file:
            line = file.readline()
            tree.insert(line)
    except IOError as error:
        print("Error with file", error)


def main():
    tree = BinaryTree()
    choice = ''
    while choice != 'x':
        choice = displayChoice()
        runFuntion(choice, tree)
    print("Exiting program")


def printTree(tree):
    # Traverse tree
    print("Inorder (sorted): ", end = "")
    tree.inorder()
    print("\nPostorder: ", end = "")
    tree.postorder()
    print("\nPreorder: ", end = "")
    tree.preorder()
    print("\nThe number of nodes is " + str(tree.getSize()))


if __name__ == '__main__':
    main()
