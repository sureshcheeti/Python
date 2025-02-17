# Write a Python program to check greatest of three numbers using Classes and Objects

class GreatestOfNumbers:

    """
        This class is used to check the greatest of three numbers.
    """
    def __init__(self,number1,number2,number3):
        
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def validate(self):

        """
           This function is return the greatest of three numbers.
        """
        if (self.number1 > self.number2) and (self.number1 > self.number3):
            return f"Given number1 {self.number1} is Greatest."
        elif (self.number2 > self.number1) and (self.number2 > self.number3):
            return f"Given number2 {self.number2} is Greatest"
        else:
            return f"Given number3 {self.number3} is Greatest."       

a = int(input("Please enter your number1 :")) # User Input
b = int(input("Please enter your number2 :")) # User Input
c = int(input("Please enter your number3 :")) # User Input
check = GreatestOfNumbers(a,b,c) # creating class object with parameter
print(check.validate())

# sample input - number1 is greatest
# a = 3
# b = 2
# c = 1
# Output : Given number1 3 is Greatest

# sample input - number2 is greatest
# a = 2
# b = 3
# c = 1
# Output : Given number2 3 is Greatest

# sample input - number3 is greatest
# a = 1
# b = 2
# c = 3
# Output : Given number3 3 is Greatest