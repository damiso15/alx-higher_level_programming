# alx-high_level_programming
* 0-run - Write a Shell script that runs a Python script.

## 0-run ##
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

~~~~
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
~~~~
