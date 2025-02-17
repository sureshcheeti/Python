
# Write a Python program to check if given number is multiple of 3 or 7 using Classes and Objects

class Multiple:

    """
        This class is used to check the given number is multiple of 3 or 7.
    """
    def __init__(self,num):
        
        self.num = num

    def validate(self):

        """
           This function is return the number is multiple of 3 or 7.
        """
        if (self.num%3==0 or self.num%7==0):
            return f"Given number {self.num} is multiple of 3 or 7."
        else:
            return f"Given number {self.num} is not multiple of 3 or 7."       

number = int(input("Please enter your number :")) # User Input
check = Multiple(number) # creating class object with parameter
print(check.validate())

# sample input - multiple of 3 or 7
# number = 21
# Output : Given number 21 is multiple of 3 or 7.

# sample input - not divisible by both
# number = 20
# output : Given number 50 is not multiple of 3 or 7.