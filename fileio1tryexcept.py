# file1tryexcept.py

#file_name = "C:\\Users\\lama2\\Pycharmprojects\\inoutput\\fileio1.py"
file_name = "not-exist"
try:
    # file_handle = open(file_name, "r")
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            print(line)
           # print(line.rstrip('\n'))
except IOError as info:
        print("Can't open " + file_name + " because " +  str(info))
#finally:
#   file_handle.close()  # Error if file doesn't exist

