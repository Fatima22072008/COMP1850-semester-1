# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
            takes the paramaters name and birth and makes sure name is a string and birth is a date
        """
        if not isinstance(name, (str)):
            raise TypeError("Should be string")
        elif name == '':
            raise ValueError("string should not be empty")

        if not isinstance(birth, (date)):
            raise TypeError("Should be string")
        
        self.birth = birth 
        self.name = name

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        this is for the initials and allows them to be split up into speerate strings then the first value is taken and then its put into uppercase
        """
        NameSeperatedValues = self.name.split()

        for values in NameSeperatedValues:
            NameInitials += values[0]
            
        return NameInitials.upper()
    
    def is_birthday(self):
        """
        checks wether its their birhtday today
         """
        if self.birth == date.today():
            return True
        else:
            return False
