# Python Week-1
Capaciti (EEE Group 1)

Altered list program

- When we assign one variable to another, we're not creating a duplicate; instead, we're assigning both variables to the same location in memory. So, if we modify one, the other will be affected as well. Understanding these concepts is crucial when writing programs and working with data in the computer's memory.

Variable                                          What is a Variable?

- A variable is a way of storing information in a computer program. Think of a variable like a container and the name of the variable as the label on the container which shows us what is inside. Variables are used in coding and programming to help coders understand, remember, and use the information in the program.
- A variable is created the moment you first assign a value to it.
- Variable names traditionally begin with lowercase letters in Python.

Types of variables in Python

- Integers, which are whole numbers.

- Strings, which are collections of characters.
- Booleans, which are true or false values, are another type of variable in Python.
- floats, which are decimal numbers.
- complex numbers, which are used for complex mathematical calculations.

#Note: Your program reads your code from top to bottom, this means that if you have assigned your variables as the following 

Kopano = Creative 

Kopano = Artistic 

The code will read as Kopano = Artistic 

#Note: If you want to name a variable multiple names use _ so for example First_Name 

---

12/03/2024

# What are Data Structures?

- Data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.

**#Note**: Data structure and data types are slightly different. Data structure is the collection of data types arranged in a specific order.

# Python Operators

- Operators are used to perform operations on variables and values.

In the example below, we use the `+` operator to add together two values:

print 7+5 

Answer = 12 

The different kinds of Operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators

## **Control flow**

 refers to the order in which statements and instructions are executed in a program. It determines how the program progresses from one instruction to another based on certain conditions and logic. Control flow mechanisms allow developers to create dynamic and flexible programs that can make decisions, repeat tasks, and respond to various inputs.

• **If Statements:** An `if` statement evaluates a condition and executes a block of code if the condition is true. It can be followed by optional `else-if` and `else` clauses to handle alternative conditions.

### **Loops**

Loops are used to repeat a block of code multiple times until a certain condition is met. They are handy for iterating over collections, performing repetitive tasks, and implementing algorithms that require repeated execution. The following types of loops are commonly used:

- **For Loops:** A `for` loop executes a block of code a fixed number of times, typically iterating over a range of values. It typically consists of an initialization statement, a condition for termination, and an increment or decrement statement.
- **While Loops:** A `while` loop repeatedly executes a block of code as long as a specified condition remains true. It evaluates the condition before each iteration, and if the condition becomes false, the loop is terminated.
- **Do-While Loops:** A `do-while` loop is similar to a `while` loop but guarantees that the code block is executed at least once. It evaluates the condition after executing the block, and if the condition is true, the loop continues.

# Functions

- Some tasks need to be performed multiple times within a program. Rather than rewrite the same code in multiple places, a function may be defined using the `def` keyword. Function definitions may include parameters, providing data input to the function.

# Python Classes/Objects

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

MyClass

we can use the class named MyClass to create objects

# The __init__() Function

- All classes have a function called __init__(), which is always executed when the class is being initiated.
- Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

The __str__() Function

- The __str__() function controls what should be returned when the class object is represented as a string.
- If the __str__() function is not set, the string representation of the object is returned

