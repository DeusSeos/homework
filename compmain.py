from linux import Linux
from windows import Windows
import re



def show_computer(computer):
    print("IP address: ", computer.ip_addr)
    print("OS: ", computer.osname)
    print("Vendor: ", computer.manufacturer)
    print("-"*40)

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
    osList = ["Linux","Windows"]
    osName = os[0]
    if osName in osList:
        return True
    else:

        return False

def addComputer():
    isValid = False
    while not isValid:
        ip = input("Input the IP of the computer: ")
        isValid = validIP(ip)
    isValid = False
    while not isValid:
        try:
            storage = input("Input the storage size of the computer: ")
            float(storage)
            isValid = True
        except ValueError as ex:
            print("{0} cannot be converted to a float: {1} \nPlease enter a valid rating.".format(storage, ex))
    isValid = False
    while not isValid:
        os = input("Enter the os to be installed on the device: ")
        os = os.split()
        isValid = validOS(os)
    isValid = False
    while not isValid:
        manufacturer = input("Enter the manufacturer: ")
        isValid = True
    isValid = False
    while not isValid:
        year = input("Enter the year: ")
        isValid = True
    print(os)
    if os[0] == 'Linux':
        a = Linux(ip)
        a.install_os(' '.join(os))
        a.manufacturer = manufacturer
        a.purchaseDate = year
    elif os[0] == 'Windows':
        a = Windows(ip)
        a.install_os(' '.join(os))
        a.manufacturer = manufacturer
        a.purchaseDate = year
    print(a)


if __name__ == '__main__':
    addComputer()