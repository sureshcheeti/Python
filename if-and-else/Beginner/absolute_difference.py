
# Write a Python program to check Find the absolute difference between two numbers; if the difference is more than 10, return double the difference.

class AbsoluteDifference:

    """
        This class is used to find the absolute difference between two numbers.
    """
    def __init__(self,num1,num2):

        self.num1 = num1
        self.num2 = num2
        self.difference = abs(self.num1-self.num2)
        
    def validate(self):

        """
           This function is return if the difference is more than 10, return double the difference.
        """
        if self.difference > 10:
            return f"Absolute difference is double with value is {self.difference*2}"
        else:
            return f"Absolute difference is {self.difference}"       

number1 = int(input("Please enter your number :")) # User Input
number2 = int(input("Please enter your number :")) # User Input
check = AbsoluteDifference(number1,number2) # creating class object with parameter
print(check.validate())

# sample input - double difference
# number1 = 30
# number2 = 10
# Output : Absolute difference is double with value is 40

# sample input - not oduble
# number1 = 30
# number2 = 25
# output : Absolute difference is 5