
# Write a Python program to check if a given character is uppercase, lowercase, digit, or special character. using Classes and Objects

class UpperLowerDigit:

    """
        This class is used to check the given character is uppercase, lowercase, digit, or special character.
    """
    def __init__(self,letter):
        
        self.letter = letter

    def validate(self):

        """
           This function is return given character is uppercase, lowercase, digit, or special character.
        """
        if ord(self.letter)>=97 and ord(self.letter)<=122:
            return f"Given character {self.letter} is lowercase."
        elif ord(self.letter)>=65 and ord(self.letter)<=90:
            return f"Given character {self.letter} is uppercase."
        elif ord(self.letter)>=48 and ord(self.letter)<=57:
            return f"Given character {self.letter} is digit."
        else:
            return f"Given character {self.letter} is special character."

character = input("Please enter your character :") # User Input
check = UpperLowerDigit(character) # creating class object with parameter
print(check.validate())

# sample input - lowercase
# character = a
# Output : Given characer a is lowercase.

# sample input - uppercase
# character = B
# output : Given character B is uppercase.

# sample input - digit
# character = 9
# output : Given character 9 is digit.

# sample input - sepcial character
# character = @
# output : Given character @ is special character.