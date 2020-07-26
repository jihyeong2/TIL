# Control_flow

>The control Statement is controlling sequential flow of code.
>
>It is image of flow chart. 

![image-20200725172727867](Python(3).assets/image-20200725172727867.png)



### 1. Conditional Statement

- `if` must include condition that judge true or false.

```python
if condition1 :
    pass
elif condition2 :
    pass
else :
    pass
```



### 2. Loop Statement

- `while` 
  - If the condition is true, execute code repeatly. 

```python
while condition :
    pass
```

- `for`
  - It tour sequence container or other iterable object sequentialy.

```python
dust = [59,24,102]
for i in dust :
    print(i)
```



### 3. Control of loop

- `break` ends loops. It escapes in `for` and `while`
- `continue` does not execute codes after `continue`.
- `pass` does not anything.