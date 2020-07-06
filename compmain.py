from linux import Linux
from windows import Windows
from linkedpriorityqueue import LinkedPriorityQueue
import re

def display(queue):
    print("\nYear Purchased{0:<6}IP Address{0:<5}Storage Space{0:<12}Operating System{0:<5}".format(' '))
    for elem in queue:
        show_computer(elem)

def removeComputer(ourComputers):
    try:
        total = input("How many computers to remove?: ").strip()
        total = int(total)
    except ValueError as ex:
        print("{0} cannot be converted to an int: {1} \nPlease enter a valid integer.".format(total, ex))
    try:
        for i in range(total):
            ourComputers.pop()
    except KeyError as ex:
        print(ex, "Please enter a number greater to or less than the number of computers in the list")

def show_computer(computer):
    print("{0:<20}{1:<15}{2:<25}{3:<15}".format(computer.purchaseDate, computer.ip_addr, computer.getSpace(), computer.osname))

def validIP(ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    if (re.search(regex, ip)):
        return True
    else:
        print("Invalid IP address")
        return False

def validOS(os):
    osList = ["linux","windows"]
    osName = os[0].lower().strip()
    if osName in osList:
        return True
    else:

        return False

def addComputer(ourComputers):
    isValid = False
    while not isValid:
        ip = input("Input the IP of the computer: ")
        isValid = validIP(ip)
    isValid = False
    while not isValid:
        try:
            storage = input("Input the storage size of the computer: ")
            storage = float(storage)
            isValid = True
        except ValueError as ex:
            print("{0} cannot be converted to a float: {1} \nPlease enter a valid storage size.".format(storage, ex))
    isValid = False
    while not isValid:
        os = input("Enter the os to be installed on the device: ")
        os = os.split()
        isValid = validOS(os)
    isValid = False
    while not isValid:
        manufacturer = input("Enter the manufacturer: ")
        if manufacturer == '':
            isValid = False
        else:
            isValid = True
    isValid = False
    while not isValid:
        try:
            year = input("Enter the year: ")
            year = int(year)
            isValid = True
        except ValueError as ex:
            print("Please enter a valid year.")

    if os[0] == 'Linux':
        a = Linux(ip)
        a.install_os(' '.join(os))
        a.FS = storage
        a.manufacturer = manufacturer
        a.purchaseDate = year
    elif os[0] == 'Windows':
        a = Windows(ip)
        a.C = storage
        a.install_os(' '.join(os))
        a.manufacturer = manufacturer
        a.purchaseDate = year
    ourComputers.add(a)


if __name__ == '__main__':
    ourComputers = LinkedPriorityQueue()
    cont = True
    while cont:
        print("\nL List all computers in your inventory")
        print("\nA Add a computer")
        print("R Remove some computers")
        choice = input("\nEnter your choice in (Q to quit): ").strip().lower()
        if choice == 'l':
            display(ourComputers)
        elif choice == 'a':
            addComputer(ourComputers)
            display(ourComputers)
        elif choice == 'r':
            removeComputer(ourComputers)
        elif choice == 'q':
            cont = False
