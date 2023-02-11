class Square:
     def __init__(self):
         self.height = 2
         self.width = 2
     def set_side(self, new_side):
         self.height = new_side
         self.width = new_side
     @property
     def height(self):
        return self._height
     @height.setter
     def height(self, value):
        self._height = value
        self._width = value
     @property
     def width(self):
        return self._width
     @width.setter
     def width(self, value):
        self._width = value
        self._height = value
  
square = Square()
square.height = 6
print (square.width)