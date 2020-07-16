from BinaryTree import BinaryTree
from Game import Game

#menus for displaying the different choices and corresponding keys that are associated with a function
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
    print("R Return to main menu\n")

# Help menu to detail what certain functions do
def helpMenu():
    print()


#This will do error checking for inputs on the order Menu and exceute the associated functions
def orderChoice(tree):
    orderMenu()
    choice = input("Enter in a display order choice: ").strip().lower()
    listChoice = ["pre", 'post', "in", "return"]
    while choice not in listChoice:
        print("\nEnter a valid choice from the menu.")
        orderMenu()
        choice = input("Enter in your choice: ").strip().lower()
    if choice == 'pre':
        tree.preorder()
        print()
    elif choice == 'post':
        tree.postorder()
        print()
    elif choice == 'in':
        tree.inorder()
        print()
    else:
        return

#error checking of the display menu choices
def displayChoice():
    displayMenu()
    listChoice = ['p', 'l', 'd', 'h', 'x']
    choice = input("Enter in your choice: ").strip().lower()
    while choice not in listChoice:
        print("\nEnter a valid choice from the menu.")
        displayMenu()
        choice = input("Enter in your choice: ").strip().lower()
    return choice

#run functions based on choice passed into function
def runFuntion(choice, tree, game):
    if choice == 'p':
        fileLoading(filename="game1.txt", tree=tree, game=game)
        play(game, tree)
    elif choice == 'l':
        newFile = input("Enter in the game file you want to load: ").strip()
        fileLoading(newFile, tree=tree, game=game)
    elif choice == 'd':
        orderChoice(tree)
    elif choice == 'h':
        helpMenu()
    else:
        return

#deals with file loading and loading data into the class of game. Deals with file read errors. Inserts the data into the tree
def fileLoading(filename, tree, game):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            game.name = line
            line = file.readline().strip()
            game.description = line
            print()
            while True:
                line = file.readline().strip()
                if not line:
                    break
                tree.insert(line)
    except IOError as error:
        print("Error with file", error)

#grabs the root of tree and traverses thru based on the input of user. Once it reaches a leaf it will print out what it thinks the answer is
def play(game, tree):
    print(game.name)
    print(game.description)
    current = tree.getRoot()
    while current.right is not None:
        message = current.element[4:] + '(Y/N): '
        while True:
            switch = input(message).strip().lower()
            if switch == 'y':
                current = current.right
                break
            elif switch == 'n':
                current = current.left
                break
            else:
                print("Please enter a valid response of T/F.")
    print(current.element[4:])

#main class which will calls necessary functions to run the game
def main():
    game = Game()
    tree = BinaryTree()

    choice = ''
    while choice != 'x':
        choice = displayChoice()
        runFuntion(choice, tree=tree, game= game)
    print("Exiting program")


if __name__ == '__main__':
    main()
