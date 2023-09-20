#1/usr/bin/python3
"""Define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a rectangle"""

    def __init__(self, size=0, x=0, y=0, id=None):
        """
        Initialize a new Square

        Args:
            size (int): Size of new Square
            x (int): x coordinate of new Square
            y (int): y coordinate of new square
            id (int): Identity of new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value size"""
        self.width = value
        self.height = value

    def __str__(self):
            """Special way pf printing"""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                    self.width)

    def update(self, *args, **kwargs):
        """
            Update class attributes

            Args:
                args (int):
                    1st argument should be the id attribute
                    2nd argument should be the size attribute
                    4th argument should be the x attribute
                    5th argument should be the y attribute
            """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] =='size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
            """Return the dictionary representation of a Square"""
            return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
