
# Write a Python program to check if triangle is valida or not based on given angles using Classes and Objects

class ValidTriangle:

    """
        This class is used to check the triangle is valida or not based on given angles.
    """
    def __init__(self,angle1,angle2,angle3):
        
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def validate(self):

        """
           This function is return triangle is valida or not based on given angles.
           - sum of all angles are equal to 180 and all angles are greater than zero.
        """
        if (self.angle1+self.angle2+self.angle3) == 180:
            return "Triangle is valid."
        else:
            return "Triangle is not valid."       

angle_1 = int(input("Please enter your angle1 :")) # User Input
angle_2 = int(input("Please enter your angle2 :")) # User Input
angle_3 = int(input("Please enter your angle3 :")) # User Input
check = ValidTriangle(angle_1,angle_2,angle_3) # creating class object with parameter
print(check.validate())

# sample input - Valid
# angle_1 = 60
# angle_2 = 40
# angle_3 = 80
# Output : Triangle is valid.

# sample input - Not Valid
# angle_1 = 50
# angle_2 = 40
# angle_2 = 20
# output : Triangle is not valid.