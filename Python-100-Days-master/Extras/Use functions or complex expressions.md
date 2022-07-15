## Use functions or complex expressions

*Larry Wall*, the original author of the Perl language, once said that great programmers have three virtues: laziness, crankiness and conceit. At first glance, none of these three words are positive words, but in the programmer's world, these three words have different meanings. First of all, laziness will prompt programmers to write some trouble-free programs to help themselves or others do their jobs better, so that we don't need to do those repetitive and tedious labor; similarly, things that can be solved with 3 lines of code, we also Never write 10 lines of code. Secondly, irritability will make programmers take the initiative to complete some work that you have not proposed, to optimize their code to make it more efficient, tasks that can be completed in 3 seconds, we must not tolerate 1 minute of waiting. In the end, conceit drives programmers to write reliable and error-free code, and we write code not to be criticized and blamed, but to be admired by others.

Then there is a very interesting question worth exploring. We need a program to find the largest number from the three input numbers. This program is a piece of cake for anyone who can program, even someone who can't program can do it after 10 minutes of learning. Below is the Python code used to solve this problem.

````Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
the_max = a
else:
the_max = b
if c > the_max:
the_max = c
print('The max is:', the_max)
````

But as we just said, programmers are lazy, and many programmers will use the ternary conditional operator to rewrite the above code.

````Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
the_max = a if a > b else b
the_max = c if c > the_max else the_max
print('The max is:', the_max)
````

It should be noted that Python did not have the ternary conditional operator used in lines 4 and 5 of the above code before version 2.5. The reason is that Guido van Rossum (the father of Python) believes that the ternary conditional operator does not Can't help Python be more concise, so those who are used to using the ternary conditional operator in C/C++ or Java (in these languages, the ternary conditional operator is also called the "Elvis operator" because `?:` Put together it looks like the big back of the famous rock singer Elvis) programmers tried to use the short-circuiting properties of the `and` and `or` operators to simulate the ternary operator, so in those days, the above code was like this written.

````Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
the_max = a > b and a or b
the_max = c > the_max and c or the_max
print('The max is:', the_max)
````

But this approach cannot be established in some scenarios, and look at the following code.

````Python
a = 0
b = -100
# The following code was expected to output the value of a, but instead got the value of b
# Because a value of 0 will be treated as False when performing logical operations
print(True and a or b)
# print(a if True else b)
````

So the ternary conditional operator was introduced after Python 2.5 to avoid the above risks (the last sentence of the above code is commented out). So, the question comes again, can the above code be written shorter? The answer is yes.

````Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', (a if a > b else b) if (a if a > b else b) > c else c)
````

But is it really good to do this? Does such a complex expression make the code a lot more obscure? We found that in actual development, many developers like to excessively use the features or syntactic sugar of a certain language, so simple multi-line codes become complex single-line expressions. Is this really good? I have asked myself this question more than once, and the answer I can give now is the following code, using a helper function.

````Python
def the_max(x, y):
return x if x > y else y


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', the_max(the_max(a, b), c))
````

In the above code, I define a helper function `the_max` to find the larger of the two values ​​passed in by the parameter, so the following output statement can call the `the_max` function twice to find the three values. The maximum number in the number, the readability of the code is now much better. It is really a good choice to replace complex expressions with auxiliary functions. The key is that after the logic of comparing the size is transferred to this auxiliary function, it can not only be called repeatedly, but also can be cascaded.

Of course, in many languages, there is no need to implement the relatively small functions at all (usually built-in functions), and the same is true for Python. Python's built-in max function takes advantage of Python's support for variable parameters, allowing multiple values ​​or an iterator to be passed in at one time and find the maximum value, so the problems discussed above are just one sentence in Python, but The idea of ​​going from complex expressions to using auxiliary functions to simplify complex expressions is very interesting, so I share it with you for a communication.

````Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', max(a, b, c))
````