## Python programming conventions

The word "custom" refers to "customary practice, conventional method, consistent practice", and the English word corresponding to this word is "idiom". Since Python has significant differences in syntax and usage from many other programming languages, as a Python developer, if you can't master these conventions, you can't write "Pythonic" code. Below we summarize some code idiomatic in Python development.

1. Make code both importable and executable.

   ````Python
   if __name__ == '__main__':
   ````


2. Determine the logical "true" or "false" in the following way.

   ````Python
   if x:
   if not x:
   ````

   **Good** code:

   ````Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': 'Luo Hao', '1002': 'Wang Dahui'}
   if name and fruits and owners:
       print('I love fruits!')
   ````

   **Bad** code:

   ````Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': 'Luo Hao', '1002': 'Wang Dahui'}
   if name != '' and len(fruits) > 0 and owners != {}:
       print('I love fruits!')
   ````

3. Be good at using the in operator.

   ````Python
   if x in items: # contains
   for x in items: # iterate
   ````

   **Good** code:

   ````Python
   name = 'Hao LUO'
   if 'L' in name:
       print('The name has an L in it.')
   ````

   **Bad** code:

   ````Python
   name = 'Hao LUO'
   if name.find('L') != -1:
       print('This name has an L in it!')
   ````

4. Swap the two values ​​without using a temporary variable.

   ````Python
   a, b = b, a
   ````

5. Construct strings from sequences.

   **Good** code:

   ````Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', ​​'d']
   name = ''.join(chars)
   print(name) # jackfrued
   ````

   **Bad** code:

   ````Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', ​​'d']
   name = ''
   for char in chars:
       name += char
   print(name) # jackfrued
   ````

6. EAFP is better than LBYL.

   EAFP - **E**asier to **A**sk **F**orgiveness than **P**ermission.

   LBYL - **L**ook **B**efore **Y**ou **L**eap.

   **Good** code:

   ````Python
   d = {'x': '5'}
   try:
       value = int(d['x'])
       print(value)
   except (KeyError, TypeError, ValueError):
       value = None
   ````

   **Bad** code:

   ````Python
   d = {'x': '5'}
   if 'x' in d and isinstance(d['x'], str) \
   and d['x'].isdigit():
       value = int(d['x'])
       print(value)
   else:
       value = None
   ````

7. Use enumerate to iterate.

   **Good** code:

   ````Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   for index, fruit in enumerate(fruits):
   print(index, ':', fruit)
   ````

   **Bad** code:

   ````Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   index = 0
   for fruit in fruits:
       print(index, ':', fruit)
       index += 1
   ````

8. Use productions to generate lists.

   **Good** code:

   ````Python
   data = [7, 20, 3, 15, 11]
   result = [num * 3 for num in data if num > 10]
   print(result) # [60, 45, 33]
   ````

   **Bad** code:

   ````Python
   data = [7, 20, 3, 15, 11]
   result = []
   for i in data:
       if i > 10:
           result.append(i*3)
   print(result) # [60, 45, 33]
   ````

9. Use zip to combine keys and values ​​to create a dictionary.

   **Good** code:

   ````Python
   keys = ['1001', '1002', '1003']
   values ​​= ['Luo Hao', 'Wang Dachui', 'Bai Yuanfang']
   d = dict(zip(keys, values))
   print(d)
   ````

   **Bad** code:

   ````Python
   keys = ['1001', '1002', '1003']
   values ​​= ['Luo Hao', 'Wang Dachui', 'Bai Yuanfang']
   d = {}
   for i, key in enumerate(keys):
       d[key] = values[i]
   print(d)
   ````

> **Note**: The content of this article comes from the Internet, and interested readers can read [Original](http://safehammad.com/downloads/python-idioms-2014-01-16.pdf).