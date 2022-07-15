## Why I chose Python

At present, the development momentum of the Python language is unstoppable at home and abroad. With its simple and elegant syntax and powerful ecosystem, Python stands out from many languages, and now it is firmly in the top three of the programming language rankings. Many Python developers in China come from Java developers, and I am no exception. I will briefly explain to you why I chose Python.

### Python vs. Java

Let's compare with a few examples how Java and Python code are written to do the same thing.

Example 1: Output "hello, world" in the terminal.

Java code:

````Java
class Test {

    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
````

Python code:

````Python
print('hello, world')
````

Example 2: Sum from 1 to 100.

Java code:

````Java
class Test {
    
    public static void main(String[] args) {
        int total = 0;
        for (int i = 1; i <= 100; i += 1) {
            total += i;
        }
        System.out.println(total);
    }
}
````

Python code:

````Python
print(sum(range(1, 101)))
````

Example 3: Two-color balls are randomly selected.

Java code:

````Java
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Test {

    /**
     * Generate random integers in the range [min, max)
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    public static void main(String[] args) {
        // Initialize the alternative red ball
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        // pick six red balls
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        // sort the red balls
        Collections.sort(selectedBalls);
        // add a blue ball
        selectedBalls.add(randomInt(1, 17));
        // output the selected random number
        for (int i = 0; i < selectedBalls.size(); ++i) {
            System.out.printf("%02d ", selectedBalls.get(i));
            if (i == selectedBalls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }
}
````

Python code:

````Python
from random import randint, sample

# Initialize the alternative red ball
red_balls = [x for x in range(1, 34)]
# Pick six red balls
selected_balls = sample(red_balls, 6)
# sort the red balls
selected_balls.sort()
# add a blue ball
selected_balls.append(randint(1, 16))
# output the selected random number
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
````

I believe, after reading these examples, you must feel that my choice of Python is justified.