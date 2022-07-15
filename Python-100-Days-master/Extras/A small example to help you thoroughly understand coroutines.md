## A small example to help you understand coroutines thoroughly

Coroutines may be one of the most confusing knowledge points in Python for beginners, and it is also an important way to implement concurrent programming in Python. Python can use multi-threading and multi-process to achieve concurrency, these two methods are relatively familiar to everyone. In fact, there is another way to achieve concurrency called asynchronous programming, and coroutines are the necessary way to achieve asynchronous programming.

The so-called coroutine can be simply understood as multiple subroutines that cooperate with each other. In the same thread, when a subprogram is blocked, we can make the program switch from one subprogram to another immediately, so as to avoid the CPU being idle due to program blocking, so that the utilization rate of the CPU can be improved, which is equivalent to using A collaborative approach speeds up program execution. Therefore, we can say succinctly: **Coroutines realize cooperative concurrency**.

Next, I will use a small example to help you understand what cooperative concurrency is. Let's take a look at the code below.

````Python
import time


def display(num):
    time.sleep(1)
    print(num)


for num in range(10):
    display(num)
````

The above code is believed to be easy for everyone to understand. The program will output numbers from 0 to 9, and output a number every 1 second, so the execution of the entire program takes about 10 seconds. It is worth noting that because there is no multi-threading or multi-process, there is only one execution unit in the program, and the sleep operation of `time.sleep(1)` will cause the entire thread to stall for 1 second. For the above code, in During this time, the CPU is completely idle and does nothing.

Let's take a look at what happens with coroutines. Since Python 3.5, the use of coroutines to achieve cooperative editing has a more convenient syntax. We can use `async` to define asynchronous functions, and `await` can be used to let a blocking subroutine give up the CPU to the cooperating one. subroutine. In Python 3.7, `asyanc` and `await` became official keywords, giving developers a sense of euphoria. Let's first look at how to define an asynchronous function.

````Python
import asyncio


async def display(num):
    await asyncio.sleep(1)
    print(num)
````

Then tap the blackboard to say the key points. Asynchronous functions are different from ordinary functions. Calling ordinary functions will get the return value, while calling asynchronous functions will get a coroutine object. We need to put the coroutine object into an event loop to achieve the effect of cooperating with other coroutine objects, because the event loop will be responsible for handling the operation of subroutine switching. subroutine.

We first code 10 coroutine objects through the following list generation, which is the same as calling the display function in the loop just now.

````Python
coroutines = [display(num) for num in range(10)]
````

The following code can get the event loop and put the coroutine object into the event loop.

````Python
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()
````

Executing the above code will find that 10 coroutines that block for 1 second each only block for about 1 second in total, which means that once the coroutine object blocks, it will give up the CPU instead of leaving the CPU idle. Status**, which greatly improves the CPU utilization**. And we will also notice that the numbers from 0 to 9 are not printed in the order in which we created the coroutine objects, which is the result we want; in addition, executing the program multiple times will find the result of each output All are not the same, which is the result of the uncertainty of the execution order of the concurrent program itself.

The above example comes from the famous "Flower Book" ("Advanced Concurrent Programming in Python"). In order to make everyone have a deeper understanding of coroutines, we have made small changes to the code of the original book. Although this example is simple, it has Let you experience the charm of collaborative concurrency. In commercial projects, if you need to use cooperative concurrency, you can also replace the system default event loop with the event loop provided by `uvloop`, which will achieve better performance, because `uvloop` is based on the well-known cross-platform asynchronous I /O library libuv implemented. In addition, if you want to do HTTP-based network programming, the three-party library **aiohttp** is a good choice, it implements asynchronous HTTP server and client based on asyncio.