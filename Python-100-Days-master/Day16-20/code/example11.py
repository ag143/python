"""
Scope of variables and the order in which Python searches for variables
LEGB: Local --> Embedded --> Global --> Built-in
global - declare or define a global variable (either directly use an existing global scope variable, or define a variable and place it in the global scope)
nonlocal - declares a variable that uses the nested scope (if the nested scope does not have a corresponding variable, an error will be reported)
"""
x = 100


def foo():
     global x
     x = 200

     def bar():
         x = 300
         print(x)

     bar()
     print(x)


foo()
print(x)