def main():
    str = "hello world!"
    print(str)

    print( myFun() )


def myFun():
    print("This is myFun()")
    num1, num2 = getNumbers()
    result = addNumbers(num1, num2)

    return result


def getNumbers() -> tuple:
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    nums = (num1, num2)
    print("in getNumbers: ", type(nums) )
    return nums


def addNumbers(x, y) -> float:
    return x + y


if __name__ == "__main__":
    main()
