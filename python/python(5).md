# Function II

### 1. Function & Scope

- The function make a space called scope in inner.  There are two scope, the one is local scope that made by function, the other is global scope out of local scope.
- Name search rule(LEGN rule)
  - Local scope : defined function.
  - Enclosed scope : upper function.
  - Global scope : variables out of function or imported module.
  - Built-in scope : function and artribute in python.
- All of variables has each lifecycle.
  - Built-in scope : 
  - global scope : after called module and for executing interpreter.
  - local scope : from called function to ended function.



### 2. Recursive function

> Recursive function is the function that recall same function in inner.

```python
def factorial(int num) :
    if num <= 0:
        return 1
    return num * factorial(num - 1)
```

