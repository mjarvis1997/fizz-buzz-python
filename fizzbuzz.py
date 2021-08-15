# prints integers 1 through N based on these rules:
#
#   if divisible by 3
#       prints Fizz
#   if divisible by 5
#       prints Buzz
#   if divisible by 3 and 5
#       prints FizzBuzz

# divisors and phrases can be changed

def printIntegers(n, divisor1, divisor2, phrase1, phrase2):

    print("Result:")

    for i in range(1,n+1):
        output = ""

        if i % divisor1 == 0:
            output += phrase1
        if i % divisor2 == 0:
            output += phrase2
        if output == "":
            output += str(i)

        print(output)

val = ""

while val != "3":

    print("")
    print("Welcome to Jarvis' FizzBuzz Solution in Python! Select an option to begin\n1: Run default FizzBuzz\n2: Customize with your own values\n3: Exit")

    val = input("")

    if val == "1":
        printIntegers(15, 3, 5, "Fizz", "Buzz")
    if val == "2":
        d1 = int(input("Enter value for first divisor: "))
        d2 = int(input("Enter value for second divisor: "))
        p1 = input("Enter value for first phrase: ")
        p2 = input("Enter value for second phrase: ")
        n = int(input("Enter value for N: "))
        printIntegers(n, d1, d2, p1, p2)

    