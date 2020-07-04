from computersystem import ComputerSystem

class Linux(ComputerSystem):


    @property
    def FS(self):
        return self._FS

    @FS.getter
    def FS(self):
        return self._FS

    @FS.setter
    def FS(self, FS):
        if FS <= 0:
            raise Exception("Cannot have storage of size less than 0")
        else:
            self._FS = FS

    def getSpace(self):
        return "Filesystem: {} GB".format(self._FS)


if __name__ == '__main__':
    a = Linux("1.1.1.1", "L")
    a.FS = 100
    b = a.getSpace()
    print(b)