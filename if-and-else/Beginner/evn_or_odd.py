# Write a Python program to check if a number is even or odd using Classes and Objects

class EvenOrOdd:

    """
        This class is used to check the given number is even or odd.
    """
    def __init__(self,num):
        
        self.num = num

    def validate(self):

        """
           This function is return the number is even or odd.
        """
        if self.num%2==0:
            return f"Given number {self.num} is Even."
        else:
            return f"Given number {self.num} is Odd."       

number = int(input("Please enter your number :")) # User Input
check = EvenOrOdd(number) # creating class object with parameter
print(check.validate())

# sample input - Even
# number = 10
# Output : Given number 10 is Even

# sample input - Odd
# number = 9
# output : Given number 9 is negative