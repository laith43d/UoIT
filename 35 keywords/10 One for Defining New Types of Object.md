#class

Used to define a template for a new type of OBJECT.

```python
from math import tau

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return self.radius * 2

    def circumference(self):
        return self.radius * tau

    def area(self):
        return tau * self.radius ** 2 / 2
```
