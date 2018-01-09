# file chaos.py
# a simple program to yada yada yada, we get the idea from the name alone
# from Python programing by John Zelle

def main():
    print("This program will illustrate a chaotic function... OR WILL IT?!!!")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()
