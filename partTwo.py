import math  

def main():
    sideOne = int(input("What is Length A?:"))
    sideTwo = int(input("What is Length B?:"))

    print(pythag(sideOne, sideTwo))

def pythag(A,B):
    result = (A**2 + B**2)
    finalResult = (result**0.5)
    return(finalResult)

main()
