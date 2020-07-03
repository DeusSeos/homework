# computersystem.py

""" This class represents a computer system

"""

class ComputerSystem():
    """Class represents a computer system

    Attributes:
        ip_addr (str): the IP address of the computer
        location (str): where the computer resides
        _os (str): the operating system of this computer
    """

    def __init__(self, ip_addr, location, date, vendor="Dell"):
        self.ip_addr = ip_addr
        self.location = location
        self._vendor = vendor
        self._purchaseDate = date


    def ls(self):
        pass

    def copy(self):
        pass

    # Note: no setter method for OS because it's set only when an
    # OS is installed
    def install_os(self, osname):
        self._os = osname

    def _get_os(self):
        """
           Get OS name installed on the computer system
        :return (str): OS name
        """
        return self._os

    osname = property(_get_os)

    def getspace(self):
        # subclass to implement
        pass

    # Using decorator
    @property
    def manufacturer(self):
        print("in manufacturer getter method")
        return self._vendor

    @manufacturer.setter
    def manufacturer(self, vendor):
        print("in manufacturer setter method")
        self._vendor = vendor

    @property
    def purchaseDate(self):
        return self._purchaseDate

    @purchaseDate.setter
    def purchaseDate(self, date):
        self._purchaseDate = date

    @purchaseDate.getter
    def purchaseDate(self):
        return self._purchaseDate

    def __str__(self):
        return "IP address: {0.ip_addr}, location: {0.location}, OS: {0._os}, manufacturer: {0._vendor}".format(self)

