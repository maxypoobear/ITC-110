Maximilian McDonald
ITC 110
HW #2

1. What are the two values of the Boolean data type? How do you write them?

A:
True and False, always with the first letter capitalized

2. What are the three Boolean operators?

A:
and, or, not

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

A:
True and True is True
True and False is False
False and True is False
False and False is True
True or True is True
True or False is True
False or True is True
False or False is False
not True is False
not False is True


4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

A:
False
False
True
False
False
True

5. What are the six comparison operators?

A:
==, !=, <, >, <=, >=

6. What is the difference between the equal to operator and the assignment operator?

A:
"==" compares two values to see if they're the same
"=" assigns a value or expresssion a variable

7. Explain what a condition is and where you would use one.

A:
A condition is an expression that evaluates to True and False. It's used for flow control.

8. Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

A:
spam = 0 BLOCK 1
if spam == 10: BLOCK 2
print('spam') BLOCK 3 

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

A:
spam = input()
if spam == 1
    print('Hello')
elif spam == 2
    print('Howdy')
else:
    print('Greetings!')

10. What can you press if your program is stuck in an infinite loop?

A:
CTRL + C

11. What is the difference between break and continue?

A:
A break statement makes the progra mexecution exit the loop it's found in and the continue statement returns the program to the top of the loop to reevaluate.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

A:
range(10) starts at 0 and ends at 10, range(0, 10) sets the lowest and highest number in the range, and range(0, 10, 1) starts at 0 and increases by 1 till it reaches 10.

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

A:
for i in range(10):
	print(i + 1)

count = 1
while count <= 10:
	print(count)
	count = count + 1


14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

A:spam.bacon()
