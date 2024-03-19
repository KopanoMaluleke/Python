# Python Week-2
Capaciti (EEE Group 1)

## Function :  19/03/2024

- A block of reusable code. You place () after the function name to invoke it
- Think of () as a pair of telephones talking to each other

Arguments  

You use def  and (f) to do  this 

##  F-string is **a way to format strings in Python**. It was introduced in Python 3.6 and aims to make it easier for users to add variables, comma separators, do padding with zeros and date format.

Return 

- Statement used to end a function and send a result back to the caller

### Scope

# The scope of a variable determines where it can be accessed and manipulated within a program. 

- Basically the variable is only accessed inside the function

```python
name = Bro #global scope 
def display_name(): 
    name = "code"  #local scope
    print(name)
```

In this case python will follow the 

L= Local

E=Enclosing 

G=Global

B=Built-in

So if you type outside the function it will give you an error :

print(name)
