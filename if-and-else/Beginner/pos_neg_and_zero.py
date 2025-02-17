
# Write a Python program to check if a number is positive, negative, or zero using Classes and Objects

class CheckNumber:

    """
        This class is used to check the given number is positive, negative or zero
    """
    def __init__(self,num):

        self.num = num

    def validate(self):

        """
           This function is return the number is positive, negative or zero.
        """
        if self.num > 0:
            return f"Given number {self.num} is Positive."
        elif self.num < 0:
            return f"Given number {self.num} is Negative."
        else:
            return f"Given number {self.num} is zero."       

number = int(input("Please enter your number :")) # User Input
check = CheckNumber(number) # creating class object with parameter
print(check.validate())

# sample input - positive
# number = 10
# Output : Given number 10 is Positive

# sample input - negative
# number = -10
# output : Given number -10 is negative

# sample input - zero
# number = 0
# output : Given number 0 is zero