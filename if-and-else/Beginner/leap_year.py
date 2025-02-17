
# Write a Python program to check if given year is leap year or not using Classes and Objects

class CheckYear:

    """
        This class is used to check the given year is leap year or not.
    """
    def __init__(self,year_value):
        
        self.year_value = year_value

    def validate(self):

        """
           This function is return the given year is leap year or not.
           - A year is a leap year if it is divisible by 4
           - except for end-of-century years which must be divisible by 400
        """
        if (self.year_value%4==0) and (self.year_value%100!=0) or (self.year_value%400==0):
            return f"Given year {self.year_value} is Leap Year."
        else:
            return f"Given year {self.year_value} is not Leap Year."       

year = int(input("Please enter your number :")) # User Input
check = CheckYear(year) # creating class object with parameter
print(check.validate())

# sample input - Leap year
# number = 2024
# Output : Given year 2024 is Leap Year.

# sample input - Not Leap Year
# number = 1978
# output : Given year 1978 is Not Leap Year.