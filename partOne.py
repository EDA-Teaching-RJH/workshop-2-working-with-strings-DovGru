def main():
    slow = input("Write a sentence to slow down:")
    
    print(myFunction(slow))

def myFunction(text):
    text2 = text.replace(" ", "...")
    return(text2)

main()
