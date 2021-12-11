"""
Classes are Student, Name, and Age

Name class encapsulates the first_name and last_name string member variables
with the Getter methods for first, last and full name as well as Setters for
first and last name.

Age class encapsulates the time difference between the birth year and present
year with Getters for birth year, present year, and age as well as Setters
for birth year and present year.

Student class is composed of the Name and Age class (due to the Student's
has-a relationship).
"""


class Name:
    """
    Name class
    """
    def __init__(self, first_name, last_name):
        """
        Constructor
        """
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        """
        Getter for first name
        """
        return self.first_name

    def get_last_name(self):
        """
        Getter for last name
        """
        return self.last_name

    def get_full_name(self):
        """
        Getter for full name
        """
        return self.first_name + ' ' + self.last_name

    def set_first_name(self, new_first_name):
        """
        Setter for first name
        """
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        """
        Setter for last name
        """
        self.first_name = new_last_name


class Age:
    """
    Age class
    """
    def __init__(self, birth_year, present_year):
        """
        Constructor
        """
        self.birth_year = birth_year
        self.present_year = present_year

    def get_birth_year(self):
        """
        Getter for birth year
        """
        return self.birth_year

    def get_present_year(self):
        """
        Getter for present year
        """
        return self.present_year

    def get_age(self):
        """
        Getter for age
        """
        return self.present_year - self.birth_year

    def set_birth_year(self, new_birth_year):
        """
        Setter for birth year
        """
        self.birth_year = new_birth_year

    def set_present_year(self, new_present_year):
        """
        Setter for present year
        """
        self.present_year = new_present_year


class Student:
    """
    Student class
    """
    def __init__(self, name, age):
        """
        Constructor
        """
        self.name = name
        self.age = age

    def get_name(self):
        """
        Getter for name
        """
        return self.name.get_full_name()

    def get_age(self):
        """
        Getter for age
        """
        return self.age.get_age()


if __name__ == '__main__':
    NAME = Name('Rob', 'Everest')
    AGE = Age(1961, 2019)
    STUDENT = Student(NAME, AGE)
    print(f"{STUDENT.get_name()} is {STUDENT.get_age()} old")
