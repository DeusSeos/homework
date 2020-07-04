from computersystem import ComputerSystem

class Windows(ComputerSystem):

    @property
    def C(self):
        return self._C

    @C.getter
    def C(self):
        return self._C

    @C.setter
    def C(self, C):
        if C <= 0:
            raise Exception("Cannot have storage of size less than 0")
        else:
            self._C = C

    def getSpace(self):
        return "C drive: {} GB".format(self._C)


if __name__ == '__main__':
    a = Windows("5.5.5.5", "Dell")
