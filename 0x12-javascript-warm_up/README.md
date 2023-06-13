# alx-high_level_programming #

# 0x12. JavaScript - Warm up #


## 0. First constant, first print ##
Write a script that prints “JavaScript is amazing”:

* You must create a constant variable called `myVar` with the value “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

~~~~
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$
~~~~


## 1. 3 languages ##
Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

~~~~
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
~~~~


## 2. Arguments ##
Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)

~~~~
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$
~~~~


## 3. Value of my argument ##
Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

~~~~
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$
~~~~


## 4. Create a sentence ##
Write a script that prints two arguments passed to it, in the following format: “ is ”

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

~~~~
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$
~~~~


##5. An Integer ##
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

~~~~
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$
~~~~


## 6. Loop to languages ##
Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

~~~~
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
~~~~


## 7. I love C ##
Write a script that prints `x` times “C is fun”

* Where `x` is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only two `console.log`
* You must use a loop (`while`, `for`, etc.)

~~~~
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$
~~~~
