# alx-high_level_programming
* 0-answer.txt - What function would you use to print the type of an object?
* 0-answer.txt - How do you get the variable identifier (which is the memory address in the CPython implementation)?
* 2-answer.txt - In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
* 3-answer.txt - In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
* 4-answer.txt - In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
* 5-answer.txt - In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
* 6-answer.txt - What do these 3 lines print?
* 7-answer.txt - What do these 3 lines print?
* 8-answer.txt - What do these 3 lines print?
* 9-answer.txt - What do these 3 lines print?
* 10-answer.txt - What do these 3 lines print?
* 11-answer.txt - What do these 3 lines print?
* 12-answer.txt - What do these 3 lines print?
* 13-answer.txt - What do these 3 lines print?
* 14-answer.txt - What does this script print?
* 15-answer.txt - What does this script print?
* 16-answer.txt - What does this script print?
* 17-answer.txt - What does this script print?
* 18-answer.txt - What does this script print?
* 19-copy_list.py - Write a function `def copy_list(l):` that returns a copy of a list.
* 20-answer.txt - Is a a tuple? Answer with `Yes` or `No`.
* 21-answer.txt - Is a a tuple? Answer with `Yes` or `No`.
* 22-answer.txt - Is a a tuple? Answer with `Yes` or `No`.
* 23-answer.txt - Is a a tuple? Answer with `Yes` or `No`.
* 24-answer.txt - What does this script print?
* 25-answer.txt - What does this script print?
* 26-answer.txt - What does this script print?
* 27-answer.txt - Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.





## 0-answer.txt ##
What function would you use to print the type of an object?

Write the name of the function in the file, without `()`.


## 0-answer.txt ##
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.


## 2-answer.txt ##
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

~~~~
>>> a = 89
>>> b = 100
~~~~


## 3-answer.txt ##
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

~~~~
>>> a = 89
>>> b = 89
~~~~


## 4-answer.txt ##
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

~~~~
>>> a = 89
>>> b = a
~~~~


## 5-answer.txt ##
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

~~~~
>>> a = 89
>>> b = a + 1
~~~~


## 6-answer.txt ##
What do these 3 lines print?

~~~~
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
~~~~


## 7-answer.txt ##
What do these 3 lines print?

~~~~
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
~~~~


## 8-answer.txt ##
What do these 3 lines print?

~~~~
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
~~~~


## 9-answer.txt ##
What do these 3 lines print?

~~~~
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
~~~~


## 10-answer.txt ##
What do these 3 lines print?

~~~~
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
~~~~


## 11-answer.txt ##
What do these 3 lines print?

~~~~
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
~~~~


## 12-answer.txt ##
What do these 3 lines print?

~~~~
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
~~~~


## 13-answer.txt ##
What do these 3 lines print?

~~~~
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
~~~~


## 14-answer.txt ##
What does this script print?

~~~~
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
~~~~


## 15-answer.txt ##
What does this script print?

~~~~
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
~~~~


## 16-answer.txt ##
What does this script print?

~~~~
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
~~~~


## 17-answer.txt ##
What does this script print?

~~~~
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
~~~~


## 18-answer.txt ##
What does this script print?

~~~~
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
~~~~


## 19-copy_list.py ##
Write a function `def copy_list(l):` that returns a copy of a list.

* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module

~~~~
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$
~~~~

**No test cases needed**


## 20-answer.txt ##
~~~~
a = ()
~~~~

Is a a tuple? Answer with `Yes` or `No`.


## 21-answer.txt ##
~~~~
a = (1, 2)
~~~~

Is a a tuple? Answer with `Yes` or `No`.


## 22-answer.txt ##
~~~~
a = (1)
~~~~

Is a a tuple? Answer with `Yes` or `No`.


## 23-answer.txt ##
~~~~
a = (1,)
~~~~

Is a a tuple? Answer with `Yes` or `No`.


## 24-answer.txt ##
What does this script print?

~~~~
a = (1)
b = (1)
a is b
~~~~


## 25-answer.txt ##
What does this script print?

~~~~
a = (1, 2)
b = (1, 2)
a is b
~~~~


## 26-answer.txt ##
What does this script print?

~~~~
a = ()
b = ()
a is b
~~~~


## 27-answer.txt ##
~~~~
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
~~~~

Will the last line of this script print `139926795932424?` Answer with `Yes` or `No`.
