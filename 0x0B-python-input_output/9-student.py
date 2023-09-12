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

        def to_json(self):
            """Retrieve dictionary representation of a Student"""
            return self.__dict__
