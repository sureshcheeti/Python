# Write a Python program to check if a number is divisible by both (5 and 11) or not using Classes and Objects

class Divisible:

    """
        This class is used to check the given number is divisible by both (5 and 11) or not.
    """
    def __init__(self,num):
        
        self.num = num

    def validate(self):

        """
           This function is return the number is divisible by both (5 and 11) or not.
        """
        if (self.num%5==0 and self.num%11==0):
            return f"Given number {self.num} is divisible by both 5 and 11."
        else:
            return f"Given number {self.num} is not divisible by both 5 and 11."       

number = int(input("Please enter your number :")) # User Input
check = Divisible(number) # creating class object with parameter
print(check.validate())

# sample input - divisible by both
# number = 55
# Output : Given number 55 is divisible by both 5 and 11.

# sample input - not divisible by both
# number = 50
# output : Given number 50 is not divisible by both 5 and 11.