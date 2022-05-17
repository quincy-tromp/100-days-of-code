#First code: classic "Hello World"
print("\n")
print("Hello World!")

#Code challenge 1 - print function
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
#End of assignment

#Use escape sequence \n for newline
print("\nHello World!\nHello World!")
#String concatenation
print("Hello" + " " + "my friend")

#input function
print("\nHello " + input("What is your name? "))

#Code challenge 1.3 - input function
print("\n")
print(len(input("What is your name? ")))

#Variables
name = input("\nWhat is your name?")
length = len(name)
print(length)

#Code challenge 1.4 - Switch around the values
print("\n")
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)