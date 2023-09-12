#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Represent a student"""

    def __init(self, first_name, last_name, age):
        """
        Initialize a new Student

        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """
            Retrieve dictionary representation of a Student.
            if attrs is a list of strings, represents only those attributes
            included in the list

            Args:
                attrs (list): Attributes to represent
            """
            if type(attrs) is list and all(type(ele) is str for ele in attrs):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
