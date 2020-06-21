def expo(base, power):
    number = base
    if power == 0:
        return 1
    for i in range(power-1):
        number = number * base

    return number

def expo_r(base, power):

    if power == 0:
        return 1
    elif power %2 == 0:
        result = (expo_r(base, power / 2))**2
        # print(result)
        return result

    elif power %2 == 1:
        result = base * expo_r(base, power-1)
        # print(result)
        return result

if __name__ == '__main__':
    base = 2
    power = 3
    print(expo(base, power))
    print("Exponential loop is O{}".format(power))
    print(expo_r(base, power))
    print("Recursive is O(log({}))".format(power))