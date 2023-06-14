# alx-high_level_programming #
# 0x13. JavaScript - Objects, Scopes and Closures #


## 0. Rectangle #0 ##
Write an empty class `Rectangle` that defines a rectangle:

* You must use the `class` notation for defining your class

~~~~
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
~~~~
