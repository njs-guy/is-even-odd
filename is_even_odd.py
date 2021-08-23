from time import sleep

class Is_even_odd:
    # Checks for even and odd
    def is_even_odd(self, x):
        if (x % 2 == 0):
            self.print_even(x)
        else:
            self.print_odd(x)
    
    # Printing results
    def print_even(self, y):
        print(str(y) + " is even.")
    
    def print_odd(self, y):
        print(str(y) + " is odd.")

# driver
iEO = Is_even_odd()
input = int(input("Enter a number and I will tell you if it is even or odd..."))
iEO.is_even_odd(input)

print("\n")

print("This will close in 15 seconds.")
sleep(15)

#exit = input("Press any key to exit...")
#print(exit)