
# Write a Python program to check if gievn character is vowel or consonant using Classes and Objects

class VowelOrConsoant:

    """
        This class is used to check the given number is even or odd.
    """
    def __init__(self,letter):
        
        self.letter = letter
        self.vowels = "aeiouAEIOU"

    def validate(self):

        """
           This function is return the number is even or odd.
        """
        if self.letter in self.vowels:
            return f"Given character {self.letter} is Vowel."
        else:
            return f"Given character {self.letter} is Consonant."       

number = input("Please enter your character :") # User Input
check = VowelOrConsoant(number) # creating class object with parameter
print(check.validate())

# sample input - vowel
# number = a
# Output : Given character a is Vowel.

# sample input - consonant
# number = b
# output : Given character b is Consonant.