def testFunction():
    print("This happens first")
    input("[Type enter to continue]")


def mathFunction(a, b, symbol):

    if symbol == "+":
        answer = a + b

    elif symbol == "-":
        answer = a - b
    else:
        answer = a * b

    print(answer)


def decreaseFunction(numList):
    # assume numList is a list of 3 numbers, eg: [9, 7, 4]. 
    numList[0] -= 1
    numList[1] -= 1
    numList[2] -= 1

def getInputAndUpdateList(myList):
    value1 = input("[type a, b, or c]")
        
    if value1 == "a":
        myList[0] += 1
    elif value1 == "b":
        myList[1] += 1
    elif value1 == "c": 
        myList[2] += 1
    else: 
        print("Choose one of the options chicken brain")
        return

def main():

    # mathFunction(3, 4, '*')
    # mathFunction(3, 4, '+')
    # mathFunction(3, 4, '-')
    # mathFunction(6, 4, '*')
    # mathFunction(6, "cat", '*')

    # tempList = [0, 7, 4]
    # decreaseFunction(tempList)
    # print(tempList)
    # decreaseFunction(tempList)
    # print(tempList)
    # decreaseFunction(tempList)
    # print(tempList)
    # decreaseFunction(tempList)
    # print(tempList)


    # ----

    print("How big is your brain?")
    input("[type enter to start]")

    myList = [0, 0, 0]

    print(
        """Can you tell when a boy likes you? 
    a. Yes - always
    b. No - never I am blind
    c. Sometimes - depends if they're obvious or not"""
    )

    getInputAndUpdateList(myList)

    print(
        """Can you rememember the score when you play volleyball?
    a. Yes - easy peasy, I always no the score
    b. No - I can never remember even when people tell me
    c. Sometimes - depends on my mood"""
    )

    getInputAndUpdateList(myList)

    print(
        """Can you remember song lyrics well?
    a. Yes - only takes me a couple listens
    b. No - my brain small
    c. Sometimes - if I listen enough"""
    )

    getInputAndUpdateList(myList)

    print("Here is your result!")
    input("[hit enter to view]")

    if myList[0] >= 2:
        print("You got a galaxy brain, good 4 u!")

    elif myList[1] >= 2:
        print("You got a chicken brain, haha.")

    elif myList[2] >= 2:
        print("You got a big brain, lame.")

    else: 
        print("You got a chicken brain, haha.")

    # print(myList)




    # tiny buzzfeed quiz
    #


    # =================================

    # value1 = input("num1 :")
    # value2 = input("num2 :")

    # print(int(value1) + int(value2))

    # =================================

    # print("Who are you? :")
    # value = input("Who are you? :")

    # print("Hello " + value)

    # ask a question

    # =================================

    # print(__name__)

    # a = 100
    # print(str(a))

    # b = "taylor swift"
    # print(b)

if __name__ == "__main__":
    main()