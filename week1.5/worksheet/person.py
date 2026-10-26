# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):

        self.name = name

        if self.name == ' ':
            raise ValueError
        elif type(self.name) != str:
            raise TypeError
        
        self.birth = birth 

        if type(self.birth) != date:
            raise TypeError
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):

        NameSeperated = self.name.split()
        for values in NameSeperated:
            NameInitials += values[0]
        return NameInitials.upper()
    
    def is_birthday(self):

        if self.birth == date.today():
            return True
        else:
            return False
