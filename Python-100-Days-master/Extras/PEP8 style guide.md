## PEP 8 Style Guide

PEP is short for Python Enhancement Proposal, usually translated as "Python Enhancement Proposal". Each PEP is a technical document for the Python community to guide Python in a better direction, among which Enhancement Proposal 8 (PEP 8) is a code style guide for the Python language. Although we can write Python code at will on the premise that there is no problem with the grammar, in actual development, writing readable code in a consistent style is what every professional programmer should do, and it is also what every professional programmer should do. The requirements set forth in the company's programming specifications are particularly important when multiple people collaborate on a project (team development). We can find this document from the [PEP 8 link](https://www.python.org/dev/peps/pep-0008/) on the official Python website, below we make a brief summary of the key parts of the document .

### Use of spaces

1. <u> Use spaces for indentation instead of tabs. </u> This is unreasonable for people who are used to other programming languages, because most programmers use Tab to indicate indentation, but you must know that Python is not like C/C++ or Java. Use curly braces to construct a block of code syntax. In Python, branching and looping structures both use indentation to indicate which code belongs to the same level. Given this Python code's dependence on indentation and indentation width is stronger than in many other languages. many. Tabs may be 2, 4 or 8 characters wide in different editors, or even other more outrageous values, and using Tab to represent indentation can be a disaster for Python code.
2. <u> Each level of indentation related to syntax is represented by 4 spaces. </u>
3. <u> The number of characters in each line should not exceed 79 characters. If the expression is too long and occupies multiple lines, the rest of the lines except the first line should be added to the normal indentation width plus 4 characters space. </u>
4. <u>The definitions of functions and classes should be separated by two blank lines before and after the code. </u>
5. <u>In the same class, each method should be separated by a blank line. </u>
6. A space should be reserved on the left and right sides of the <u> binary operator, and only one space should be used. </u>

### Identifier naming

PEP 8 advocates different naming styles for naming different identifiers in Python, so that when reading code, the name of the identifier can determine what role the identifier plays in Python (at this point, Python's own The built-in modules, as well as some third-party modules, are not very well done).

1. <u>Variables, functions, and properties should be spelled in lowercase letters, with underscores if there are multiple words. </u>
2. <u>A protected instance property in a class, which should start with an underscore. </u>
3. <u> Private instance properties in a class should start with two underscores. </u>
4. <u>Names of classes and exceptions should capitalize the first letter of each word. </u>
5. <u> Module-level constants should be in all uppercase letters. If there are multiple words, connect them with underscores. </u>
6. Instance methods of the <u> class should name the first parameter `self` to represent the object itself. </u>
7. The class method of the <u> class should name the first parameter `cls` to represent the class itself. </u>

### Expressions and Statements

In the Zen of Python (you can use `import this` to view) there is a famous saying: "There should be one-- and preferably only one --obvious way to do it.", translated into Chinese is "do one thing should be There is, and preferably only, one exact way of doing it", the idea conveyed in PEP 8 is also ubiquitous.

1. <u> takes the negation inline, instead of putting the negation in front of the whole expression. </u> For example `if a is not b` is easier to understand than `if not a is b`.
2. Do not use the length check method to determine whether a string, list, etc. is `None` or has no elements. Instead, use `if not x` to check it.
3. <u> Even if there is only one line of code in the `if` branch, `for` loop, `except` exception catch, etc., do not write the code together with `if`, `for`, `except`, etc., and write them separately will make the code clearer. </u>
4. The <u>`import` statement is always placed at the beginning of the file. </u>
5. <u>When importing a module, `from math import sqrt` is better than `import math`. </u>
6. <u>If there are multiple `import` statements, they should be divided into three parts, from top to bottom are Python **standard modules**, **third-party modules** and **custom modules* *, inside each section should be in **alphabetic order** of the module name. </u>