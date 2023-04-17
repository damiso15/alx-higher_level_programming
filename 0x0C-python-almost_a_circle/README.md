# alx-high_level_programming
* tests/ - All your files, classes and methods must be unit tested and be PEP 8 validated
* models/base.py, models/__init__.py - Write the first class `Base`
* models/rectangle.py - Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded)
* models/rectangle.py - Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance
* models/rectangle.py - Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.
* models/rectangle.py - Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
* models/rectangle.py - Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character # by taking care of `x` and `y`
* models/rectangle.py - Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute




## tests/ ##
All your files, classes and methods must be unit tested and be PEP 8 validated.

~~~~
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
~~~~

*Note that this is just an example. The number of tests you create can be different from the above example.*



## models/base.py, models/__init__.py ##
Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py:`

* Class `Base:`
	* private class attribute `__nb_objects = 0`
	* class constructor: `def __init__(self, id=None):`:
		* if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
		* otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

~~~~
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 
~~~~


## models/rectangle.py ##
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

* If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
* If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
* If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

~~~~
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$ 
~~~~


## models/rectangle.py ##
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance

~~~~
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$
~~~~


## models/rectangle.py ##
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.
~~~~
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$
~~~~


## models/rectangle.py ##
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

~~~~
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$
~~~~


## models/rectangle.py ##
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character # by taking care of `x` and `y`

~~~~
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
guillaume@ubuntu:~/$
~~~~


## models/rectangle.py ##
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute
* 1st argument should be the `id` attribute
* 2nd argument should be the `width` attribute
* 3rd argument should be the `height` attribute
* 4th argument should be the `x` attribute
* 5th argument should be the `y` attribute

This type of argument is called a “no-keyword argument” - Argument order is super important.

~~~~
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$
~~~~
